<template>
    <div>
      <h2>Posts in #{{ $route.params.category }}</h2>
      <PostList :posts="posts" v-if="posts" />
    </div>
  </template>
  
  <script>
  import PostList from '@/components/PostList'
  import gql from 'graphql-tag'

  export default {
    async created () {
    const posts = await this.$apollo.query({
      query: gql`query ($category: String!) {
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
      }`,
      variables: {
        category: this.$route.params.category,
      },
    })
    this.posts = posts.data.postsByCategory
  },
    name: 'PostsByCategory',
    components: {
      PostList,
    },
    data () {
      return {
        posts: null,
      }
    },
  }
  </script>