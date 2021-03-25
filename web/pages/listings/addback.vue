<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-12 mb-4 text-center my-3">
        <form @submit.prevent="submitListings">
          <div class="form-group">
            <h1>Categories</h1>

          <div class="form-group">
            <label for>Categories</label>
            <select v-model="listings.category">
              <option v-for="list in categories" :key="list.id" :value="list.id">{{ list.name }}</option>
            </select>
          </div>


          <div class="form-group">
            <label for>Categories</label>
            <div class="row" v-bind:class="{selected: selectedList === list}" v-for="list in categories" v-on:click="listFilter(list)" v-model="listings.category">
              {{ list.name }}
            </div>
            <p>{{selectedList}}</p>
          </div>










          <div class="form-group">
            <label for>Name</label>
            <input type="text" class="form-control" v-model="listings.name">
          </div>
          <div class="form-group">
            <label for>Price</label>
            <input type="numer" class="form-control" v-model="listings.price">
          </div>
          <img
            v-if="preview"
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            :src="preview"
           alt>
          <img
            v-else
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            src="@/static/placeholder.png">
          <br></br>
          <div class="form-group">
            <label for>Image</label>
            <input type="file" name="image" @change="onFileChange">
          </div>
          <div class="form-group">
            <label for>Description</label>
            <textarea v-model="listings.description" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
      </div>
              </form>
      </div>
      <div class="col-md-6 mb-4">

      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitListings">
          <div class="form-group">








          </div>


        </form>
      </div>
    </div>
  </main>
</template>


<script>
export default {
  head() {
    return {
      title: "Add Listings"
    };
  },
  name: "node",
  middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        errorMessage () {
            const {error} = this
            if (!error || typeof error === 'string') {
                return error
            }
            let msg = ''
            if (error.message) {
                msg += error.message
            }
            if (error.errors) {
                msg += `(${JSON.stringify(error.errors)
                    .replace(/[{}"[\]]/g, '')
                    .replace(/:/g, ': ')
                    .replace(/,/g, ' ')})`
            }
            return msg
        }
    },
    data(){
        return{
            selected: [],
            categoriesid:[],
            value: false,
            nameRules: [
                    v => !! v || 'Any contents is required'
                ],
      visible: "",
      selectedList: [],
      list: [],
     listings: 
     {
        name: "",
        category: "",
        description: "",
        price: "",
        image: "",
        secondimage: "",
        images:[],
        error: null
      },
      preview: ""
    };
  },
    async asyncData({$axios, params}) {
        try{
            let categories = await $axios.$get(`/server/categorieslist/`)
            console.log(categories)
            return{ categories}
        } catch{}
            console.log()
    },
  methods: {
      toggleChildren() {
        this.showChildren = !this.showChildren;
      },
      listFilter: function(list) {
            this.selectedList = list;
        },
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.listings.image = files[0]
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitListings() {

      this.error = null

      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.listings) {
        formData.append(data, this.listings[data]);
      }
      try {
        let response = await this.$axios.$post("/server/createlistings/", formData, config);
        this.$router.push("/");
      } catch (e)  {
        this.error = e.response.data
      }
    }
  }
};
</script>

<style scoped>
</style>