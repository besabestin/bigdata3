<template>
    <form @submit.prevent="addItem" class="mb-4">
        <div class="mb-2">
            <label class="block text-gray-700">Item Name</label>
            <input v-model="name" type="text" class="w-full p-2 border rounded" required />
        </div>
        <div class="mb-2">
            <label class="block text-gray-700">Quantity</label>
            <input v-model="quantityValue" type="number" class="w-full p-2 border rounded" required />
        </div>
        <div class="mb-2">
            <label class="block text-gray-700">Quantity Type</label>
            <select v-model="quantityTypeId" class="w-full p-2 border rounded">
                <option v-for="type in quantityTypes" :key="type.id" :value="type.id">{{ type.type }}</option>
            </select>
            <input v-model="newQuantityType" type="text" placeholder="Add new type" class="w-full p-2 border rounded mt-2" />
        </div>
        <button type="submit" class="bg-blue-500 text-white p-2 rounded">Add Item</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            quantityValue: '',
            quantityTypeId: null,
            newQuantityType: '',
            quantityTypes: []
        };
    },
    methods: {
        async fetchQuantityTypes() {
            const response = await fetch('http://localhost:8003/quantity-types');
            this.quantityTypes = await response.json();
        },
        async addItem() {
            if (this.newQuantityType) {
                const response = await fetch('/api/quantity-types', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type: this.newQuantityType })
                });
                const newType = await response.json();
                this.quantityTypeId = newType.id;
            }
            await fetch('/api/items', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: this.name,
                    quantity_type_id: this.quantityTypeId,
                    quantity_value: this.quantityValue
                })
            });
            this.$emit('item-added');
            this.name = '';
            this.quantityValue = '';
            this.quantityTypeId = null;
            this.newQuantityType = '';
        }
    },
    mounted() {
        this.fetchQuantityTypes();
    }
};
</script>