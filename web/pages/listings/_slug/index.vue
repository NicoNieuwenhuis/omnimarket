<template>
  <main class="container my-5">
    <div class="row">



      
        <div class="col-md-2" style="float: left">
          <div class="overflow-y-auto" style="height: 300px; overflow-y: auto;">
              <img class="thumbnails" :src="listings.thumbnail" v-on:mouseover="img = listings.firstimage">
              <img class="thumbnails" :src="listings.secondthumbnail" v-on:mouseover="img = listings.secondimage">                          
            <div v-for="image in listings.images">
              <img class="thumbnails" :src="image.imagethumbnail" v-on:mouseover="img = image.image">
            </div>
          </div>
          </div>
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
          <br>
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
    </div>
    <tabs fill class="flex-column flex-md-row">
    <card shadow>
        <tab-pane title="Description">
            <span slot="title">
                <i class="fa fa-bars" aria-hidden="true"></i>
                Description
            </span>
            <p>{{listings.description}}</p>
        </tab-pane>
         <tab-pane>
             <div slot="title">
                <i class="fa fa-map" aria-hidden="true"></i>
                Map
              </div>
            <p class="description">Raw denim you probably haven't heard of them jean shorts
                Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                keffiyeh dreamcatcher synth.</p>
        </tab-pane>
        <tab-pane title="comments" >
              <div slot="title" @click="getComments">
                <i class="fa fa-comments" aria-hidden="true"></i>
                Comments
            </div>
            <p>{{comment}}<p>
              <p v-for="comment in comment">
                {{comment.content}}
                </p>
        </tab-pane>
         <tab-pane>
             <div slot="title">
                <i class="fa fa-question" aria-hidden="true"></i>
                Q&A
              </div>
            <p class="description">Raw denim you probably haven't heard of them jean shorts
                Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                keffiyeh dreamcatcher synth.</p>
        </tab-pane>
        <tab-pane>
             <span slot="title">
                <i class="fa fa-user-circle" aria-hidden="true"></i>
                User
              </span>
            <p class="description">Raw denim you probably haven't heard of them jean shorts
                Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                keffiyeh dreamcatcher synth.</p>
        </tab-pane>
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
      images: [],
      img: "",
      comment: "",
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

    getComments() {
      fetch('/server/commentslistings/'+this.$route.params.slug+'/')
        .then(response => response.json())
        .then((data) => {
          this.comment = data;

        })
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