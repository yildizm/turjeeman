import Promise from "bluebird";
import appState from "../../../../utility/app_state";

class LoginService {
    loginUser(user = {}) {
        return Promise.try(() => {
            let {password, username} = user;
            fetch('auth/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: user.username,
                    password: user.password,
                })
            })
            .then((resp) => resp.json()) // Transform the data into json
            .then(function(data) {
                if(data.response === 'OK'){
                    let user = {username: data.username, name:data.name, surname:data.surname}
                    return appState.setUser(user);
                }
                else{
                    console.log("Wrong credentials");
                }
            })
        });
    }

    logoutUser() {
        return Promise.try(() => {
            return appState.clearUser();
        });
    }
}

export default new LoginService();
