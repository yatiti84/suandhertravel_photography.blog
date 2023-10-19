import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Post from "@/components/PagePost";
import Author from "@/components/PageAuthor";
import PostsByTag from "@/components/PostsByTag";
import PostsByCategory from "@/components/PostsByCategory";
import AllPosts from "@/components/AllPosts";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  { path: "/author/:username", component: Author },
  { path: "/post/:slug", component: Post },
  { path: "/tag/:tag", component: PostsByTag },
  { path: "/category/:category", component: PostsByCategory },
  { path: "/AllPosts", component: AllPosts },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
