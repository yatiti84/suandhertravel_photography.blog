<template>
  <p v-if="error">Something went wrong...</p>
  <p v-if="loading">Loading...</p>
  <div class="post" v-if="post">
    <h2>{{ post.title }}: {{ post.subtitle }}</h2>
    By
    <AuthorLink :author="post.author" />
    <div>{{ displayableDate(post.publishDate) }}</div>
    <p class="post__description">{{ post.metaDescription }}</p>
    <article>
      {{ post.body }}
    </article>
    <ul>
      <li class="post__tags" v-for="tag in post.tags" :key="tag.name">
        <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </div>
</template>
  
<script>
import AuthorLink from '@/components/AuthorLink'
import gql from 'graphql-tag'
import { ref, watch } from 'vue'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'

const postQuery = gql`query ($slug: String!) {
          postBySlug(slug: $slug) {
            title
            subtitle
            publishDate
            metaDescription
            slug
            body
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
  name: 'PagePost',
  components: {
    AuthorLink,
  },
  setup() {
    const route = useRoute()
    console.log(route)
    const routeName = route.params.slug
    const post = ref(null);
    const { result, loading, error } = useQuery(postQuery, { slug: routeName });
    watch(
      () => result.value,
      (newPost) => {
        post.value = newPost ? newPost.postBySlug : null;
      },
      { immediate: true } // Trigger the watcher immediately
    );
    return {
      post,
      loading,
      error
    }
  },
  methods: {
    displayableDate(date) {
      return new Intl.DateTimeFormat(
        'en-US',
        { dateStyle: 'full' },
      ).format(new Date(date))
    }
  },
}
</script>