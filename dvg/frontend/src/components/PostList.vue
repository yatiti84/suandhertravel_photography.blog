<template>
    <div>
      <ol class="post-list">
        <li class="post" v-for="post in publishedPosts" :key="post.title">
            <span class="post__title">
              <router-link
                :to="`/post/${post.slug}`"
              >{{ post.title }}: {{ post.subtitle }}</router-link>
            </span>
            <span v-if="showAuthor">
              by <AuthorLink :author="post.author" />
            </span>
            <div class="post__date">{{ displayableDate(post.publishDate) }}</div>
          <p class="post__description">{{ post.metaDescription }}</p>
          <ul>
            <li class="post__tags" v-for="tag in post.tags" :key="tag.name">
              <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
            </li>
          </ul>

          <ul>
            <li class="post__categories" v-for="category in post.categories" :key="category.name">
              <router-link :to="`/category/${category.name}`">#{{ category.name }}</router-link>
            </li>
          </ul>
        </li>
      </ol>
    </div>
  </template>

<script>
import AuthorLink from '@/components/AuthorLink'
import { ref, watch, onBeforeMount } from 'vue';

export default {
  name: 'PostList',
  components: {
    AuthorLink,
  },
  props: {
    posts: {
      type: Array,
      default: () => [],
      required: true,
    },
    showAuthor: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  setup(props) {
    const publishedPosts = ref([]);
    // const publishedPosts = computed(() => {
    //   return props.posts.filter(post => post.published);
    // });
    
    watch(() => {
      publishedPosts.value = props.posts.filter(post => post.published);
    });
    // Before the component is mounted, filter the published posts
    onBeforeMount(() => {
      publishedPosts.value = props.posts.filter(post => post.published);
    });


    // Use a reactive reference to track the posts
    
    // const publishedPosts = ref(props.posts || []);
    // // const publishedPosts = ref([]);
    // watch(() => {
    //   publishedPosts.value = props.posts;
    // });
    // Watch for changes in the props.posts and update the local posts
    // watchEffect(() => {
    //   if (props.posts) {
    //     postsRef.value = props.posts;
    // //     const publishedPosts = computed(() => {
    // //   return postsRef.value.filter(post => post.published);
    // // });
    // //     return {
    // //   publishedPosts
    // // }
    //   }
    // });

    // const publishedPosts = computed(() => {
    //   return postsRef.value.filter(post => post.published);
    // });
    // computed(() => {
    //   return publishedPosts.value.filter(post => post.published);
    // });

    return {
      publishedPosts
    }
  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat(
        'zh-TW',
        { dateStyle: 'full' },
      ).format(new Date(date))
    }
  },
}
</script>

<style>
.post-list {
  list-style: none;
}

.post {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.post__title {
  font-size: 1.25rem;
}

.post__description {
  color: #777;
  font-style: italic;
}

.post__tags {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
}
</style>