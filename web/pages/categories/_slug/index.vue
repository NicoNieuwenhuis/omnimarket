<template>
<main>
    <div class="container page" >
      <div class="row" >
      <div class="col-xs-12 col-md-3">
  <div class="panel panel-default pd-search-filter">
    <div class="panel-heading">
      <h3 class="panel-title"><i class="fa fa-circle-o"></i> By Category</h3>
    </div>
    <div class="panel-body">
      <ul class="filter-category" v-for="list in categories">
        <ListCategorie v-if="list.parent == null" :node="list" :category='categoriedetail.id'></ListCategorie>
      </ul>
    </div>
  </div>
  </div>
    <b-container class="col-xs-12 col-md-9">
    <div class="row" >
      <template v-for="listing in listings">
           <div :key="listing.id" class="col-md-4">
              <listing-card :listing="listing"></listing-card>
          </div>
      </template>
    </div>
</b-container>
  </div>
</div>
</div>
</main>
</template>

<script>
import CatListCard from "~/components/CatListCard.vue";
export default {
  props: {
    node: Object
  },
  head() {
    return {
      title: "Listings list"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let listings = await $axios.$get(`/server/categorylistings/${params.slug}/`);
      let categories = await $axios.$get(`/server/categorieslist/`);
      let categoriedetail = await $axios.$get(`/server/categorydetail/${params.slug}/`);
      return { listings, categories, categoriedetail };
    } catch (e) {
      return { listings: [], categories: [], categoriedetail:[] };
    }
  },
  data() {
    return {
      listings: [],
      categories: [],
    };
  },
  methods: {
    async deleteListing(listing_id) {
      try {
        await this.$axios.$delete(`/server/listings/${listing_id}/`); 
        let newListings = await this.$axios.$get("/server/listings/"); 
        this.listings = newListings; 
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
title {
    display: block;
}
.carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 130px;
    left: 15%;
    z-index: 10;
    padding-top: 20px;
    padding-bottom: 20px;
    color: #fff;
    text-align: center;
    font-size: 75px;
}
</style>
