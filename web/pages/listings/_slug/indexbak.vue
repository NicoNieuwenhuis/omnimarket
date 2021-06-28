<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-6">
        <div style="width: 500px; height: 275px;">
      <img style="max-width: 500px; max-height: 300px;" v-if="img" :listing="listings"
          class="img-fluid"
          :src="img"
          alt>
      <img style="max-width: 500px; max-height: 300px;" v-else :listing="listings"
          class="img-fluid"
          :src="listings.firstimage"
          alt>
        </div>
          <hr>
      </div>
      <div class="col-md-4">
                <h1 class="mb-3 display-4 text-uppercase">{{ listings.name }}</h1>
          <div v-if="this.listings.hasprice === true">
            <h2>Price</h2>
            <h2>{{listings.price}}</h2>            
          </div>
          <nuxt-link :to="`/listings/${listings.slug}-${listings.id}/edit`" >
          <div v-if="$auth.$state.loggedIn">
            <button v-if="author" class="btn btn-primary">Edit</button>
          </div>
          </nuxt-link>
      </div>
        <div class="col-md-10" style="float: left">
          <div class="colums">
              <img class="thumbnails" :src="listings.firstimage" v-on:mouseover="img = listings.firstimage">
              <img class="thumbnails" :src="listings.secondimage" v-on:mouseover="img = listings.secondimage">                          
            <div v-for="image in listings.images">
              <img class="thumbnails" :src="image.image" v-on:mouseover="img = image.image">
            </div>
          </div>
          </div>
    </div>
<tabs fill class="flex-column flex-md-row">
    <card shadow>
        <ul class="tabs-choose">
          <li @click="activeTab ='1'" class="[activeTab === '1' ? 'active' : ''] ">Description</li>
          <li v-on:click="getComments" @click="activeTab ='2'" class="[activeTab === '2' ? 'active' : '']">Comments</li>
        </ul>
        <div class="tabs-content">
          <div class="content-one" v-if="activeTab === '1'">
           <p>{{listings.description}}</p> {{this.listings.description}}
          </div>
          <div class="content-twoo" v-if="activeTab === '2'">Content twoo</div>
        </div>
    </card>
</tabs>
  </main>
</template>


<script>
import axios from "axios";

export default {
  auth: false,
  middleware: ['auth'],
  data() {
    return {
      activeTab:"1",
      images: [],
      img: "",
      comments: [],
      listing:[]
    }
  },
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        author() {
            return this.$auth.user.pk == this.listings.author;
        },
        users() {
            return this.$auth.user.pk == this.comments.author;
        },
    },
    head(){
        return{
            title: 'view listings'
        }
    },
    async asyncData({$axios, params}) {
        try{
            let listings = await $axios.$get(`/server/listings/${params.slug}/`)
            console.log(listings)
            return{ listings}
        } catch{}
            console.log()
    },
  methods: {
    async getComments() {
        try{
          let comments = axios.get('/server/commentslistings/'+this.$route.params.slug+'/')
            console.log(comments)
            return{ comments}
        } catch{}
            console.log()
    },
  	isActive (menuItem) {
      return this.activeItem === menuItem
    },
    setActive (menuItem) {
      this.activeItem = menuItem
    }
  }
};
</script>

<style>
.thumbnails{ 
  width: 100px;
  height: 60px;
  float: left;
}
</style>