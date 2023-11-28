<template>
  <div>
    <h2>Posts in #{{ $route.params.tag }}</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <PostList :posts="posts" v-if="posts" />
  </div>
</template>

<script>
import PostList from '@/components/PostList'
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'

const postsByTagQuery = gql`query ($tag: String!) {
  postsByTag(tag: $tag) {
    title
    subtitle
    publishDate
    published
    metaDescription
    slug
    author {
      user {
        username
        firstName
        lastName
      }
    }
    tags {
    slug
      name
    }
    categories {
    slug
      name
    }
  }
},
`


export default {
  name: 'PostsByTag',
  setup() {
    const route = useRoute()
    const routeName = route.params.tag
    const { result, loading, error } = useQuery(postsByTagQuery, {
      tag: routeName,
    }
    );
    return {
      posts: result.value ? result.value.postsByTag : null,
      loading,
      error
    }
  },
  components: {
    PostList,
  },
  data() {
    return {
      postsByTag: null,
    }
  },
}
</script>