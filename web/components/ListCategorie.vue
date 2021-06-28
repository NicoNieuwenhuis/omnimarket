<template>

    <div>
        <!--parent-->
        <a :class="{active: node.id === categoryId}" v-if="isFolder" href="javascript:" @click="toggle">
          <span class="fa fa-fw" :class="icon"></span>
          <nuxt-link :to="`/categories/${node.slug}-${node.id}/`">
            {{node.name}}
          </nuxt-link>
        </a>
        <!--if not folding, we do not need an binding event-->
        <a v-else href="javascript:" :title="node.name" :class="{active: node.id === categoryId}" @click="filterByCategory(node.id)">
          <span class="fa fa-fw fa-circle-o"></span>
          <nuxt-link :to="`/categories/${node.slug}-${node.id}/`">
            {{node.name}}
          </nuxt-link>
        </a>
        <!--children-->
        <div v-if="isFolder" :class="isShow">
            <node v-for="child in node.children" :node="child" :search="search" :category="categoryId"></node>
        </div>
    </div>
</template>

<script>
export default {
  name: "node",
  props: ['node', 'category', 'search'],
  data() {
    return {
      open: false,
      categoryId: this.category
    }
  },
  mounted() {
    let isNodeOpen = (d) => d.id === this.categoryId || d.children && d.children.some(isNodeOpen);
    this.open = isNodeOpen(this.node);
  },
  computed: {
    icon() {
      return {
        'fa-plus': !this.open,
        'fa-minus': this.open,
      }
    },
    isFolder() {
      return this.node.children && this.node.children.length
    },
    isShow() {
      return this.open ? 'show' : 'hide'
    }
  },
  methods: {
    toggle() {
      this.open = !this.open
    },
    filterByCategory(id) {
      this.categoryId = id
    }
  }
};
</script>

<style>
.show {
  display: block !important;
}

.hide {
  display: none !important;
}
</style>