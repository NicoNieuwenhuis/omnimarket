<template>
  <div>
    <div
      :class="{bold: isFolder}"
      @click="toggle" v-on:click="setSelect(item)">
      {{ item.name }}
    </div>
    <div v-show="isOpen" v-if="isFolder" v-on:click="setSelect(item)">
      <TreeItem
        class="item"
        v-for="(child, index) in item.children"
        :key="index"
        :item="child"/>
    </div>
  </div>

</template>

<script>
import { EventBus} from '~/plugins/EventBus';
export default {
  name: "TreeItem",
  props: {
    item: Object
  },
  data: function () {
    return {
      isOpen: false,
      selected: []
    }
  },
  computed: {
    isFolder: function () {
      return this.item.children &&
        this.item.children.length
    }
  },
  methods: {
    toggle: function () {
      if (this.isFolder) {
        this.isOpen = !this.isOpen
      }
    },
    setSelect(item) {
            EventBus.$emit('clicked', item.id);
        }
  }
}
</script>

<style>
ul {
  padding-left: 1em;
  line-height: 1.5em;
  list-style-type: dot;
}

body {
  font-family: Menlo, Consolas, monospace;
  color: #444;
}

.item {
  cursor: pointer;
}

.bold {
  font-weight: bold;
}
</style>
