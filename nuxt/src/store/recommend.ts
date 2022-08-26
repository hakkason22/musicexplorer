const state = {
    show_recommend: false as boolean,
};

const mutations = {
    setShowRecommend(state: any, show_flag: boolean) {
        state.show_recommend = show_flag;
    }
}

const recommend = {
    state: state,
    mutations: mutations
};

export default recommend;
