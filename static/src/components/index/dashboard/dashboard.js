import React, { PropTypes } from "react";
import { Link } from "react-router";

import { Table, Column, Cell } from "@blueprintjs/table";

import appState from "../../../utility/app_state.js" 

import ProjectListing from "./project_listing/project_listing";

import "./_assets/style.css";

class Dashboard extends React.Component {
    constructor (props, context, ...args) {
        super(props, context, ...args);
        this.state = {
            projects: [],
        };
    }

    componentDidMount () {
        let user = appState.getUser();

        let username = user.username;
        // @TODO Replace with the actual backend function
        fetch('storage/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                status: 'fetch',
            })
        })
        .then((resp) => resp.json()) // Transform the data into json
        .then(data => {
            if(data.response === 'OK'){
                this.setState({
                    projects: [
                        {
                            id: data.id,
                            title: data.title,
                            sourceLanguage: data.source_lang,
                            targetLanguage: data.target_lang,
                            lastSaved: data.timestamp,
                        },
                    ],
                })
            }
            else{
                throw{errorMessage: "Wrong credentials"};
            }
        }).catch(error => console.error(error));
    }

    renderProjectListing (project) {
        let { id, title, sourceLanguage, targetLanguage, lastSaved } = project;

        return (
            <Link style={{color: "black"}} to={`/edit/${id}`}>
                <ProjectListing
                    projectID={id}
                    projectTitle={title}
                    sourceLanguage={sourceLanguage}
                    targetLanguage={targetLanguage}
                    lastSaved={lastSaved}
                />
            </Link>
        );
    }

    newProject () {
        // @TODO Send request to get an id.
        let user = appState.getUser();

        let username = user.username;
        let retrievedID = 123;

        let { router } = this.context;

        fetch('storage/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                status: 'create',
            })

        })
        .then((resp) => resp.json()) // Transform the data into json
        .then(data => {
            if(data.response === 'OK'){
                console.log(data.id)
                retrievedID = data.id;
                console.log("asd")
                console.log(retrievedID);
                router.push("/edit/" + data.id);
            }
            else{
                throw{errorMessage: "Wrong credentials"};
            }
        }).catch(error => console.error(error));

        //let retrievedID = 123;

        

        
    }

    render () {
        let { projects } = this.state;

        return (
            <div className="center-wh">
                <h1  style={{paddingTop: 100}}>
                    Dashboard
                </h1>
                <button
                    onClick={this.newProject.bind(this)}
                    type="button"
                    className="pt-button pt-intent-success"
                    style={{margin: 50}}>
                    New project
                    <span className="pt-icon-standard pt-align-right" />
                </button>
                <div className="center-wv">
                    <p className="table-el">Project Title</p>
                    <p className="table-el">Source Language</p>
                    <p className="table-el">Target Language</p>
                    <p className="table-el">Last Saved</p>
                </div>
                {projects.map(this.renderProjectListing.bind(this))}
            </div>
        );
    }
}

Dashboard.contextTypes = {
    router: PropTypes.object
};

export default Dashboard;
