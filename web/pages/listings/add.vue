<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-md-12 mb-4 text-center my-3">
        <form @submit.prevent="submitListings">
          <div>
 <div class="form-group">
            <label for>Categories</label>
            <TreeView :data="categories" @nodeSelect="nodeSelect" :contextMenu="false" :renameNodeOnDblClick="false"></TreeView>
          </div>
          <div v-if="this.listings.category">
              <select  v-model="catpricetype">
                <option v-for="pricetype in categoriesid.pricetype" :key="pricetype" :value="pricetype">{{ pricetype }}</option>
              </select>
          </div>
          </br>                      
            <div class="col-md-4" style="float: right;">            
              <div class="form-group">
                <label for>Name</label>
                <input type="text" class="form-control" v-model="listings.name">
              </div>
              <div v-if="this.pricetype.price === true" class="form-group">
                <label for>Price</label>
                <input type="numer" class="form-control" v-model="listings.price">
              </div>
            </div>
            <div class="col-md-8" style="float: left;">            
              <img @click="onButtonClick"
                v-if="preview"
                class="img-fluid"
                style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
                :src="preview" alt>
              <div v-else @click="onButtonClick" style="background-color: #f4f4f4; width: 400px; height: 400px; line-height: 400px; border-radius: 10px; border: 2px solid #d9d9d9; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);">
                <div>
                  <span class="fa fa-upload fa-3x"></span>
                </div>
              </div>  
            <div class="form-group">
              <input type="file" ref="uploader" name="image" @change="onFileChange" hidden>
            </div>
            </div>
            </div>
            </br>
            <div class="col-12 text-center my-3" style="float: left;">
              <div v-if="preview" class="imageupload"  @click="onButtonClick2">
                <div  class="image-preview" v-if="preview2">
                  <img class="preview" :src="preview2" style="width: 88px; height: 88px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);">
                </div>
                <div v-else>
                <div >
                  <span class="fa fa-upload fa-3x"></span>
                </div>
                </div>
                <div>

                  <input name="image"
                  ref="uploader2"
                  class="d-none"
                  type="file"
                  accept="image/*"
                  @change="onFileChange2">
                </div>
              </div>

<div >

        <div  class="imageupload" @click="onButtonClick3" v-for="(file, key) in files">
            <img class="preview3" v-bind:ref="'preview3'+parseInt(key)"/>

        </div>

        <div v-if="preview2" class="imageupload" @click="onButtonClick3">
            <input type="file" id="files" ref="files" multiple v-on:change="handleFiles3()" hidden/>
            <span class="fa fa-upload fa-3x"></span>
        </div>

</div>        
            </div>
            </br>
            <div class="col-12 text-center my-3" style="float: left;">
              <div class="form-group">
                <label for>Description</label>
                <textarea v-model="listings.description" class="form-control" rows="8"></textarea>
              </div>
                <button type="submit" class="btn btn-primary">Submit</button>          
            </div>
          </form>
        </div>
      </div>
    </main>
  </template>


<script>
import axios from "axios"
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
            catpricetype: [],
            files: [],     
            selected: [],
            categoriesid:[],
            value: false,
            nameRules: [
                    v => !! v || 'Any contents is required'
                ],
      visible: "",
      selectedList: [],
      pricetype: "loading",
     listings: 
     {
        name: "",
        category: "",
        description: "",
        pricetype:"",
        price: "",
        hasprice: "",
        images:[],
        firstimage: "",
        secondimage: "",
        bid: "",
        payment: "",
        error: null
      },
      preview: "",
      preview2: ""
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
    handleFiles3() {
      let uploadedFiles = this.$refs.files.files;
      for(var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i]);
      }
      this.listings.images = uploadedFiles[0]
      this.getImagePreviews3();
    },
    onButtonClick3() {
      this.isSelecting = true
      window.addEventListener('focus', () => {
        this.isSelecting = false
      }, { once: true })
      this.$refs.files.click()
    },
    getImagePreviews3(){
      for( let i = 0; i < this.files.length; i++ ){
        if ( /\.(jpe?g|png|gif)$/i.test( this.files[i].name ) ) {
            let reader = new FileReader();
            reader.addEventListener("load", function(){
                this.$refs['preview3'+parseInt(i)][0].src = reader.result;
            }.bind(this), false);
            reader.readAsDataURL( this.files[i] );
        }else{
            this.$nextTick(function(){
                this.$refs['preview3'+parseInt(i)][0].src = '/img/generic.png';
            });
          }
        }
    },
      toggleChildren() {
        this.showChildren = !this.showChildren;
      },
      listFilter: function(list) {
            this.selectedList = list;
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
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.listings.firstimage = files[0]
      this.createImage(files[0]);
    },
    onFileChange2(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.listings.secondimage = files[0]
      this.createImage2(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    createImage2(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview2 = e.target.result;
      };
      reader.readAsDataURL(file);
    },   
    async submitListings() {
      this.error = null
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      this.$axios.defaults.xsrfCookieName = 'csrftoken'
      this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN" 
      let formData = new FormData();
      formData.append('category', this.listings.category);
      formData.append('pricetype', this.listings.pricetype);
      formData.append('name', this.listings.name);
      formData.append('firstimage', this.listings.firstimage);
      formData.append('secondimage', this.listings.secondimage);
      formData.append('hasprice', this.pricetype.price);
        for (let file of this.files) {
            formData.append("images", file, file.name);
        }
      try {
        let response = await this.$axios.$post("/server/create-listing/", formData, config, );
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
img.preview3 {
    width: 88px;
    height: 88px;
    box-shadow: rgb(0 0 0 / 70%) 0px 1rem 1rem;
}
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