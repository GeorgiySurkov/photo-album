Vue.component('modal', {
    template: '#modal-template'
})


new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        images: [
            {
                id: 1,
                name: 'kotik.jpg',
                file_url: '/media/images/kotik.jpg',
                thumbnail_url: '/media/thumbnail/kotik.jpg',
                showModal: false,
            },
            {
                id: 2,
                name: 'kotik2.jpg',
                file_url: '/media/images/kotik2.jpg',
                thumbnail_url: '/media/thumbnail/kotik2.jpg',
                showModal: false,
            },
        ],
        pageNumber: 0,

    },
    methods: {
        nextPage() {
            this.pageNumber++;
        },
        prevPage() {
            this.pageNumber--;
        }
    },
    computed: {
        pageCount() {
            let l = this.listData.length,
                s = this.size;
            return Math.ceil(l / s);
        },
        paginatedData() {
            const start = this.pageNumber * this.size,
                end = start + this.size;
            return this.listData
                .slice(start, end);
        }
    },
});
