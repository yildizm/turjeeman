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
				body:{
					'username': this.username,
					'password': this.password,
					/*JSON.stringify({ 
					firstParam: {username}, 
					secondParam: {password},*/
				}	
//.replace(/{|}/gi, "")
			}).then(response => response.json())
			.then(response => {
				console.log(response.json);
			}); 
			/*.then(function(responseObj){			
				console.log('status: ', responseObj.status);
				if(responseObj.status == 200){
					console.log('status: ', responseObj.status);
					let user = {username: "x", name: "y", surname: "z"};
		            return appState.setUser(user);
				}		
			})*/
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
