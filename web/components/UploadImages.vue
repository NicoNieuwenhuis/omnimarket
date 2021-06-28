<template>
    <div class="container">


        <div class="imageupload" @click="onButtonClick" v-for="(file, key) in files">
            <img class="preview" v-bind:ref="'preview'+parseInt(key)"/>

        </div>

        <div class="imageupload" @click="onButtonClick">
            <input type="file" id="files" ref="files" multiple v-on:change="handleFiles()" hidden/>
            <span class="fa fa-upload fa-3x"></span>
        </div>

    </div>
</template>
<script>
export default {
  head() {
    return {
      title: "Add Listings"
    };
  },
  data() {
    return {
        files: []
    }
  },
  methods: {
    handleFiles() {
      let uploadedFiles = this.$refs.files.files;

      for(var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i]);
      }
      this.getImagePreviews();
    },
    onButtonClick() {
      this.isSelecting = true
      window.addEventListener('focus', () => {
        this.isSelecting = false
      }, { once: true })

      this.$refs.files.click()
    },
    getImagePreviews(){
      for( let i = 0; i < this.files.length; i++ ){
        if ( /\.(jpe?g|png|gif)$/i.test( this.files[i].name ) ) {
            let reader = new FileReader();
            reader.addEventListener("load", function(){
                this.$refs['preview'+parseInt(i)][0].src = reader.result;
            }.bind(this), false);
            reader.readAsDataURL( this.files[i] );
        }else{
            this.$nextTick(function(){
                this.$refs['preview'+parseInt(i)][0].src = '/img/generic.png';
            });
          }
        }
    },
    removeFile( key ){
      this.files.splice( key, 1 );
      this.getImagePreviews();
    }
  }
}
</script>
<style>
img.preview {
    width: 88px;
    height: 88px;
    box-shadow: rgb(0 0 0 / 70%) 0px 1rem 1rem;
}
</style>