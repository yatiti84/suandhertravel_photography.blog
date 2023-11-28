<template>
  <div v-if="authorByUsername">
    <h2>{{ authorByUsername.user.firstName }} {{ authorByUsername.user.lastName }}</h2>
    <a :href="authorByUsername.website" target="_blank" rel="noopener noreferrer">Website</a>
    <p>{{ authorByUsername.bio }}</p>

    <h3>Posts by {{ authorByUsername.user.firstName }} {{ authorByUsername.user.lastName }}</h3>
    <PostList :posts="authorByUsername.postSet" :showAuthor="false" />
  </div>
</template>
  
<script>
import PostList from '@/components/PostList'
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
// import { computed } from 'vue'
const authorByUsernameQuery = gql`query ($username: String!) {
        authorByUsername(username: $username) {
          website
          bio
          user {
            firstName
            lastName
            username
          }
          postSet {
            title
            subtitle
            publishDate
            published
            metaDescription
            slug
            tags {
              name
            }
            categories {
            name}
          }
        }
      }`
export default {
  name: 'PageAuthor',
  setup() {
    const route = useRoute()
    console.log(route.params)
    const routeName = route.params.username
    const { result, loading, error } = useQuery(authorByUsernameQuery, {
      username: routeName
    });
    const authorByUsername = result.value ? result.value.authorByUsername : null
    // const fullName = computed(() => authorByUsername.user.firstName &&
    //   authorByUsername.user.lastName &&
    //   `${authorByUsername.user.firstName} ${authorByUsername.user.lastName}`
    // ) || `${authorByUsername.user.username}`

    // `${firstName.value} ${lastName.value}`);

    // const displayName = () => {
    //   return fullName.value
    // }
    return {
      authorByUsername,
      loading,
      error,
    }
  },
  components: {
    PostList,
  },
  data() {
    return {
      author: null,
    }
  },
  // computed: {

  // },
}
</script>