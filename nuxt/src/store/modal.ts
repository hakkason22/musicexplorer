const state = {
    target_modal_type: "" as string,
};

const mutations = {
    showModal(state: any, modal_type: string){
        state.target_modal_type = modal_type;
    },
    closeModal(state: any){
        state.target_modal_type = "";
    }
};

const modal = {
    state: state,
    mutations: mutations,
};

export default modal;
