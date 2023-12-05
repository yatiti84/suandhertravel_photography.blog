<template>
  <nav>
    <div class="navbar-container">
      <button @click="toggleMenu">☰ Menu</button>
      <ul :class="{ 'show': isMenuOpen }">
        <li @click="closeMenu"><router-link to="/">Home</router-link></li>
        <li @click="closeMenu"><router-link to="/blog">Blog</router-link></li>
        <li @click="closeMenu"><router-link to="/about">About</router-link></li>
        <li class="submenu" @click="toggleCategoryMenu" @mouseover="openCategoryMenu" @mouseout="closeCategoryMenu">
          <span color="">Categories</span>
          <ul v-show="isCategoryMenuOpen" @mouseover="openCategoryMenu" @mouseout="closeCategoryMenu">
            <li v-for="cate in categories" :key="cate.name">
              <router-link @click="closeMenu" :to="`/category/${cate.name}`">{{ cate.name }}</router-link>
            </li>
            <!-- <li><router-link @click="closeMenu" to="/category/category1">Category 1</router-link></li>
            <li><router-link @click="closeMenu" to="/category/category2">Category 2</router-link></li> -->
            <!-- Add more categories as needed -->
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import gql from 'graphql-tag'
import { ref, watch } from 'vue'
import { useQuery } from '@vue/apollo-composable'
const categoriesQuery = gql`
query {
  allCategories{
    name
    slug
  }
}`
export default {
  data() {
    return {
      isMenuOpen: false,
      isCategoryMenuOpen: false,
      // categoryList: [{ name: 'euro' }, { name: 'japan' }, { name: 'tw' }]
    };
  },
  setup() {
    const categories = ref(null);
    const { result, loading, error } = useQuery(categoriesQuery);

    // Watch for changes in the GraphQL response data
    watch(
      () => result.value,
      (newCategories) => {
        categories.value = newCategories? newCategories.allCategories : null;
      },
      { immediate: true } // Trigger the watcher immediately
    )
    return {
      categories,
      loading,
      error,
    }
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
      this.isCategoryMenuOpen = false;
    },
    toggleCategoryMenu() {
      this.isCategoryMenuOpen = !this.isCategoryMenuOpen;
    },
    openCategoryMenu() {
      this.isCategoryMenuOpen = true;
    },
    closeCategoryMenu() {
      if (!this.isMenuOpen) {
        this.isCategoryMenuOpen = false;
      }
    },
    closeMenu() {
      this.isMenuOpen = false;
      this.isCategoryMenuOpen = false;
    },
  },
};
</script>

<style scoped>
nav {
  background-color: #D6B183;  
  /* Set the background color of the entire navbar to red */
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

button {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
}
span {
  color:#634D32;
    text-decoration: none;
    font-weight: bold;
}
ul {
  list-style: none;
  padding: 0;
  display: flex;
}

li {
  margin: 0 10px;
}

.submenu {
  position: relative;
}

.submenu ul {
  position: absolute;
  top: 100%;
  left: 0;
  display: none;
  background-color: #D6B183;  
  /* Set the background color of the submenu to red */
  list-style: none;
  padding: 0;
}

.submenu:hover ul,
.submenu ul.show {
  display: block;
  /* Keep the submenu visible when clicking on the category or submenu */
}

.submenu ul li {
  padding: 10px;
}

/* Media Query for Small Screens */
@media only screen and (max-width: 600px) {
  .navbar-container {
    flex-direction: column; /* Change the direction to column for small screens */
  }

  ul {
    flex-direction: column;
    text-align: center; /* Center align the items for small screens */
  }

  li {
    margin: 10px 0;
  }

  .submenu ul {
    top: 0; /* Adjust the position of the submenu for small screens */
  }
}
</style>