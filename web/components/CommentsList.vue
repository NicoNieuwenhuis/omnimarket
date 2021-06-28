<template>
  <div class="list comment-list">
    <div >
      <h5 class="comment-list-title">{{ comment.content }}</h5>
    </div>
  </div>
</template>

<script>
export default {
    props: ["comment"]
};
</script>

<style>

</style>