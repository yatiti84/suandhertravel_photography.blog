<template>
  <div>
    <h2>Recent posts</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <PostList v-else :posts="posts" />
  </div>
</template>
  
<script>
import PostList from '@/components/PostList'
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
const postsQuery = gql`query {
        allPosts {
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
      name
    }
    categories {
      name
    }
  }
        }`
export default {
  name: 'AllPosts',
  setup() {
    const { result, loading, error } = useQuery(postsQuery);
    console.log(result)
    const posts = result._rawValue.allPosts
    console.log(posts)
    // this.posts = posts
    // this.allPosts = posts.allPosts
    return {
      posts,
      loading,
      error
    }
  },
  components: {
    PostList,
  },

  data() {
    return {
      allPosts: null,
    }
  },
}
</script>