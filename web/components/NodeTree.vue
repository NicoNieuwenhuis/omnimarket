<template>
    <li>
        <!--parent-->
        <a v-if="isFolder" href="javascript:" @click="toggle">
            <span class="fa fa-fw" :class="icon"></span> {{node.name}}
        </a>
        <!--if not folding, we do not need an binding event-->
        <a v-else href="javascript:" :title="node.name" :class="{active: node.id === categoryId}" @click="filterByCategory(node.id)"><span class="fa fa-fw fa-circle-o"></span> {{node.name}}</a>
        <!--children-->
        <ul v-if="isFolder" :class="isShow">
            <list-category v-for="child in node.children" :key="index" :node="child" :search="search" :category="categoryId"></list-category>
        </ul>
    </li>
</template>

<script>
export default {
  props: ['node', 'category', 'search'],
  node() {
    return {
      open: false,
      categoryId: this.category
    }
  },
  mounted() {
    let isDataOpen = (d) => d.id === this.categoryId || d.children && d.children.some(isDataOpen);
    this.open = isDataOpen(this.node);
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