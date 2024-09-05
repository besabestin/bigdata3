<template>
    <div>
        <ul>
            <li v-for="item in items" :key="item.id" class="flex items-center mb-2">
                <input type="checkbox" @change="markAsBought(item.id)" :checked="item.bought" class="mr-2" />
                <span :class="{ 'line-through': item.bought }">{{ item.name }} - {{ item.quantity_value }} {{ getQuantityType(item.quantity_type_id) }}</span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: ['items'],
    methods: {
        async markAsBought(itemId) {
            await fetch(`http://localhost/items/${itemId}/bought`, { method: 'PUT' });
            this.$emit('item-updated');
        },
        getQuantityType(id) {
            const type = this.$root.quantityTypes.find(type => type.id === id);
            return type ? type.type : '';
        }
    }
};
</script>