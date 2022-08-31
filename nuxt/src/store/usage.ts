
const state = {
    max_page: 4 as number,
    usage_page: 1 as number,
};

const mutations = {
    next_usage_page(state: any) {
        if (state.usage_page >= state.max_page){
            return
        }
        state.usage_page += 1;
    },
    back_usage_page(state: any){
        if (state.usage_page <= 1){
            return
        }
        state.usage_page -= 1;
    },
}

const getters = {
    show_usage_page: (state:any) => (number:number)=>{
        if (state.usage_page == number){
            return true
        }else{
            return false
        }
    },
}

const usage = {
    state: state,
    mutations: mutations,
    getters: getters,
};

export default usage;