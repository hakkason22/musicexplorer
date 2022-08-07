const state = {
    loading_state: false as boolean,
  };
  
  const mutations = {
    loading_state (state: any, loading_state: boolean) {
      state.loading_state = loading_state;
    }
  };
  
  const loading = {
    state: state,
    mutations: mutations,
  };
  
  export default loading;
  