<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-12 mb-4 text-center my-3">
        <form @submit.prevent="submitListings">
      <div class="col-12 text-center my-3">
          <div class="form-group">
            <label for>Categories</label>
            <TreeView :data="categories" @nodeSelect="nodeSelect" :contextMenu="false" :renameNodeOnDblClick="false"></TreeView>
          </div>
          <div>
              <select v-model="catpricetype">
                <option v-for="pricetype in categoriesid.pricetype" :key="pricetype" :value="pricetype">{{ pricetype }}</option>
              </select>
          </div>
      </div>
        <br></br>
     <div class="col-md-6 mb-4" style="float: left;"> 
        <img v-if="this.listings.image" class="preview" :src="this.listings.image" style="width: 550px; height: auto; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);" alt>
        <img v-else class="img-fluid" style="width: 550px; height: auto; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);" src="@/static/placeholder.png">
        <br></br>
        <div class="form-group">
        <div>
        <div>
            <div class="file-upload-form">
                <v-btn 
                :loading="isSelecting"
                @click="onButtonClick2">
                    <span class="fa fa-fw fa-plus"></span>
                    {{ buttonText }}
                </v-btn>
            <input name="image2"
            ref="uploader2"
            class="d-none"
            type="file"
            accept="image/*"
            @change="previewImage2">                
            </div>
        </div>
        </div>
      </div>
      </div>
      <div class="col-md-4" style="float: right;">
          <div class="form-group">
            <label for>Name</label>
            <input type="text" class="form-control" v-model="listings.name">
          </div>
          <div class="form-group" v-if="pricetype.price === true">
            <label for>Price</label>
            <input type="numer" class="form-control" v-model="listings.price">
          </div>
      </div>
        <br></br>
      <div class="col-12 text-center my-3" style="float: left;">
      <div class="form-group">
        <div class="imageupload"  @click="onButtonClick">
          <div  class="image-preview" v-if="listings.secondimage.length > 0">
                <img class="preview" :src="listings.secondimage" style="width: 88px; height: 88px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);">
          </div>
          <div @click="onButtonClick" v-else>
            <v-btn >
            <span class="fa fa-upload fa-3x"></span>
            {{ buttonText }}
            </v-btn>
          </div>
          <div>

            <input name="image"
            ref="uploader"
            class="d-none"
            type="file"
            accept="image/*"
            @change="previewImage">
          </div>
        </div>
        <div>

            <UploadImages v-if="listings.secondimage.length > 0"></UploadImages>

        </div>
      </div>
        </br>

      <div class="col-12 text-center my-3" style="float: left;">



          <div class="form-group">
            <label for>Description</label>
            <textarea v-model="listings.description" class="form-control" rows="8"></textarea>
          </div>
          <input type="file" name="image" @change="onFileChange">
          <button type="submit" class="btn btn-primary">Submit</button>
      </div> 
      </div>         

        </form>
      <div class="col-md-6 mb-4">
      </div>
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
import axios from "axios"
import EventBus from '~/plugins/EventBus';
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
        },
    icon() {
      return {
        'fa-plus': !this.open,
        'fa-minus': this.open,
      }
    },
    isFolder() {
      return this.list.children && this.list.children.length
    },
    isShow() {
      return this.open ? 'show' : 'hide'
    }
    },
    data(){
        return{
            selected: [],
            categoriesid:[],
            pricetype:[],
            catpricetype:[],
            imageData: "",
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
  mounted() {
    let isNodeOpen = (d) => d.id === this.categoryId || d.children && d.children.some(isNodeOpen);
    this.open = isNodeOpen(this.list);
  },
  methods: {
    toggle() {
      this.open = !this.open
    },
    onButtonClick() {
      this.isSelecting = true
      window.addEventListener('focus', () => {
        this.isSelecting = false
      }, { once: true })

      this.$refs.uploader.click()
    },
    onButtonClick2() {
      this.isSelecting = true
      window.addEventListener('focus', () => {
        this.isSelecting = false
      }, { once: true })

      this.$refs.uploader2.click()
    },
    previewImage: function(event) {
      // Reference to the DOM input element
      var input = event.target;
      // Ensure that you have a file before attempting to read it
        if (input.files && input.files[0]) {
          // create a new FileReader to read this image and convert to base64 format
          var reader = new FileReader();
          // Define a callback function to run, when FileReader finishes its job
          reader.onload = (e) => {
            // Note: arrow function used here, so that "this.imageData" refers to the imageData of Vue component
            // Read image as base64 and set to imageData
              this.listings.secondimage = e.target.result;
          }
          // Start the reader job - read file as a data url (base64 format)
          reader.readAsDataURL(input.files[0]);
        }
     },
     previewImage2: function(event) {
        // Reference to the DOM input element
        var input = event.target;
        // Ensure that you have a file before attempting to read it
          if (input.files) {
            // create a new FileReader to read this image and convert to base64 format
            var reader = new FileReader();
            // Define a callback function to run, when FileReader finishes its job
            reader.onload = (e) => {
              // Note: arrow function used here, so that "this.imageData" refers to the imageData of Vue component
              // Read image as base64 and set to imageData
              this.listings.image = e.target.result;
            }
            // Start the reader job - read file as a data url (base64 format)
            reader.readAsDataURL(input.files[0]);
          }
      },        
    toggle() {
      this.open = !this.open
    },
    onFileChange(e) {
      this.selectedFile = e.target.files[0]
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
    },
    nodeSelect(node, isSelected) {
      console.log('Node ' + node.data.name + ' has been ' + (isSelected ? 'selected' : 'deselected'))
        if (isSelected) {
            this.listings.category = node.data.id
            this.categoriesid = node.data
        } else if (node.data === this.selectedNode) {
            this.selected = null
      }
    },
    getPricetype() {
      axios.get ("/server/pricetypedetail/" + this.catpricetype + "/")
      .then (response => {
        this.pricetype = response.data;
      })
      .catch (e => {
        this.errors.push (e)
      })
    }
  },
  watch: {
    catpricetype: {
      handler: 'getPricetype',
      immediate: true
    },
  }
};
</script>

<style>
span.fa.fa-upload.fa-3x {
    line-height: 80px;
}

.imageupload {
    float: left;
    width: 100px;
    height: 100px;
    border: 2px solid #d9d9d9;
    padding: 4px 4px 4px 4px;
    margin: 4px 4px 4px 4px;
}
</style>