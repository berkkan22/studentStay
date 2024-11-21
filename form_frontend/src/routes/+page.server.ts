export const actions = {
  submit: async ({ request }) => {
    // TODO log the user in
    console.log("HI")
    const data = await request.formData();
    console.log(data)
  },

};