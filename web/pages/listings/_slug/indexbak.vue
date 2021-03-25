<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h1 class="mb-3 display-4 text-uppercase">{{ listings.name }}</h1>
      </div>
      <div class="col-md-6 mb-4">
      <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="listings.image"
          alt>
      </div>
      <div class="col-md-4">
          <div>
            <h2>Price</h2>
            <h2>{{listings.price}}</h2>            
          </div>
          <nuxt-link :to="`/listings/${listings.slug}/edit`" >
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
                <i class="ni ni-cloud-upload-96"></i>
                Description
            </span>
            <p>{{listings.description}}</p>
        </tab-pane>
        <tab-pane title="comments" >
            <button slot="title" @click="getComments()">
                <i class="ni ni-bell-55 mr-2"></i>
                Comments
            </button>
            <div>
              <p>{{comments.content}}</p>
              <template v-for="comment in comments">
                <div :key="comment.id">
                    <listing-card :comment="comment"></listing-card>
                </div>
              </template>
            </div>
        </tab-pane>
        <tab-pane>
             <span slot="title">
                <i class="ni ni-calendar-grid-58"></i>
                Messages
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
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        author() {
            return this.$auth.user.pk == this.listings.author_id;
        },
    },
    head(){
        return{
            title: 'view listings'
        }
    },
    data() {
      return {
        comments: []
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
    async submitListings({$axios, listings}) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.listings) {
        formData.append(data, listings[data]);
      }
      try {
        let response = await this.$axios.$post("/server/listings/${listings.slug}/", formData, config);
        this.$router.push("/listings/");
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>

<style>

</style>