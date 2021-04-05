<template>
  <div id="divContent">
    <h1>Article Search Results</h1>
    <form v-on:submit.prevent="loadUsers">
      <input type="text" v-model="query">
      <button type="submit">Search</button>
    </form>
<button class="btn btn-primary" @click="getData">Get Todos</button>



    <ul>
    <li>
      {{ articles }}
    </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data () {
    return {
      articles: 'loading',
    }
  },
  watch: {
    articles() {
      this.$emit('update:articles', this.articles)
    }
  },
  methods: {
    getData() {
      axios.get ('/server/pricetypedetail/price/')
      .then (response => {
        this.articles = response.data;
      })
      .catch (e => {
        this.errors.push (e)
      })
    },
  }
};
</script>