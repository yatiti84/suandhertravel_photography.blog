import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'

import { DefaultApolloClient } from '@vue/apollo-composable'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
  cache,
  uri: 'http://localhost:8000/graphql',
//   link: 'http://localhost:8000/graphql'
})

const app = createApp({
    setup () {
    provide(DefaultApolloClient, apolloClient)
  },
  render: () => h(App),
})
app.use(router)
app.mount('#app')






