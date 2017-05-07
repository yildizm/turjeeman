import Promise from "bluebird";
import appState from "../../../../utility/app_state";

class LoginService {
    loginUser(user = {}) {
        return Promise.try(() => {
            let {password, username} = user;
			fetch('auth/data', {
				method: 'POST', 
				headers: { 
					'Accept': 'application/json', 
					'Content-Type': 'application/json', 
				}, 	
				body:JSON.stringify({ 
					firstParam: {username}, 
					secondParam: {password},
				}	
//.replace(/{|}/gi, "")
			}).then(response => response.json())
			.then(response => {
				console.log(response.json);
			});	
            if (password === "123456" && username === "deneme") {
                let user = {username: "Baraa", name: "Baraa", surname: "Orabi"};
                return appState.setUser(user);
            } else {
                throw {errorMessage: "Wrong credentials"};
            }
        })
    }

    logoutUser() {
        return Promise.try(() => {
            return appState.clearUser();
        });
    }
}

export default new LoginService();
