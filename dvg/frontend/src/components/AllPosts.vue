<template>
    <div>
      <h2>Recent posts</h2>
      <p v-if="error">Something went wrong...</p>
      <p v-if="loading">Loading...</p>
      <PostList v-else :result="allPosts" />

      <!-- <PostList v-else v-for="post in result.allPosts" :key="character.id">
        {{ character.name }} -->
      <!-- </p>
      <PostList v-if="allPosts" :posts="allPosts" /> -->
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
    // this.allPosts = posts.data.allPosts
  export default {
    name: 'AllPosts',
    components: {
      PostList,
    },
    setup () {
    const { result, loading, error } = useQuery(postsQuery);
    return {
      result,
      loading, 
      error
    }
   },
    data () {
      return {
          allPosts: null,
      }
    },
  }
  </script>