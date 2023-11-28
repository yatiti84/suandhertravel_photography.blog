<template>
  <div id="app">
    <header>
      <h1>雨女攝影旅遊suanddhertravel Blog</h1>

      <router-link to="/">Home</router-link>

      <router-link to="/about">About</router-link>
      <router-link to="/AllPosts">allposts</router-link>

    </header>
    <!-- <p v-if="error">Something went wrong...
    {{ error }}</p>
  <p v-if="loading">Loading...</p>
  <p v-else>{{ result }}</p> -->
  </div>
  <nav>
    <router-view />
  </nav>
</template>
<script>
export default {
  name: 'App',
}
</script >
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

/* ### */
* {
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 1.5rem;
}

*+* {
  margin-top: 1.5rem;
}

#app {
  margin: 0;
  padding: 0;
}
</style>

<!-- <script>
export default {
  name: 'App',
}
</script> -->
