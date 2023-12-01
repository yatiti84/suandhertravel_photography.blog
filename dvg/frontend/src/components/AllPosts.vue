<template>
  <div>
    <h2>Recent posts</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <p v-if="posts === null">Loading...</p>
    <PostList v-else :posts="posts" />
  </div>
</template>

<script>
import PostList from '@/components/PostList'
import gql from 'graphql-tag'
import { ref, watch } from 'vue'
import { useQuery } from '@vue/apollo-composable'

const postsQuery = gql`
  query {
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
        slug
      }
    }
  }
`

export default {
  name: 'AllPosts',
  components: {
    PostList,
  },
  setup() {
    const posts = ref(null);
    const { result, loading, error } = useQuery(postsQuery);

    // Watch for changes in the GraphQL response data
    watch(
      () => result.value,
      (newPosts) => {
        posts.value = newPosts ? newPosts.allPosts : null;
      },
      { immediate: true } // Trigger the watcher immediately
    );

    return {
      posts,
      loading,
      error,
    };
  },
};
</script>
