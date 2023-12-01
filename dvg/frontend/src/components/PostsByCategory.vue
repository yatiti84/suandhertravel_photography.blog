<template>
  <div>
    <h2>Posts in #{{ $route.params.category }}</h2>
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
import { ref, watch } from 'vue'

const postsByCategory = gql`query ($category: String!) {
        postsByCategory(category: $category) {
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
          name}
        }
      }`

export default {
  name: 'PostsByCategory',
  setup() {
    const route = useRoute()
    const routeName = route.params.category
    const posts = ref(null);
    const { result, loading, error } = useQuery(postsByCategory, {
      category: routeName,
    }
    );
    watch(
      () => result.value,
      (newPosts) => {
        posts.value = newPosts ? newPosts.postsByCategory : null;
      },
      { immediate: true } // Trigger the watcher immediately
    );
    return {
      posts,
      loading,
      error
    }
  },
  components: {
    PostList,
  }
}
</script>