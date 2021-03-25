<template>

  <div class="drow">
  <listing-card v-for="listing in node.listing" :listing="listing"></listing-card>
    <node v-if="node.children" v-for="child in node.children" :node="child">
    </node>
  </div>
</template>

<script>
export default {
  name: "node",
  props: {
    node: Object
  },
    data(){
        return{
      visible: "",
      }
    }
};
</script>
<style>
.drow {
    display: flex;
    /* flex-wrap: wrap; */
    margin-right: 25px;
    margin-left: 25px;
}
</style>