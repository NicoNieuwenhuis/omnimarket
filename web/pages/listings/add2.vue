<template>
    <div class="container">
    <form>
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <div class="panel panel-default">
                    <div class="panel-heading">VUe Example Component</div>

                    <div class="panel-body">
                            <legend>Upload form</legend>

                            <div class="form-group">
                                <label>Upload Files</label>
                                <input id="upload-file" type="file" multiple class="form-control" @change="fieldChange">
                            </div>

              <div class="form-group">
                <label for>Name</label>
                <input type="text" class="form-control" v-model="name">
              </div>


                            <button class="btn btn-primary" @click="uploadFile">Submit</button>

                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</template>

<script>
    export default {
        data(){
          return {
              attachments:[],
              listings:{
              name:"",
              images:[]
              }
          }
        },
        methods:{
            fieldChange(e){
                let selectedFiles=e.target.files;
                if(!selectedFiles.length){
                    return false;
                }
                for(let i=0;i<selectedFiles.length;i++){
                    this.attachments.push(selectedFiles[i]);
                }
                console.log(this.attachments);
            },
            uploadFile(){

      this.error = null

      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      this.$axios.defaults.xsrfCookieName = 'csrftoken'
      this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN" 
      let formData = new FormData();

      const data = new FormData();

      data.append('name', this.name);

        for (let file of this.files) {
            data.append("files", file, file.name);
        }

      data.append('images', this.listings.images);

      try {
        let response = this.$axios.$post("/server/create-listing/", data, config, );
        this.$router.push("/");
      } catch (e)  {
        this.error = e.response.data
      }
    },
        mounted() {
            console.log('Component mounted.')
        }
    }
}
</script>