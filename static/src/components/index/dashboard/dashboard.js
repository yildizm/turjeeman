import React, { PropTypes } from "react";
import { Link } from "react-router";

import { Table, Column, Cell } from "@blueprintjs/table";

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
        // @TODO Replace with the actual backend function
        fetch('storage', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        })
        .then((resp) => resp.json()) // Transform the data into json
        .then(data => {
            if(data.response === 'OK'){
                console.log(data.title)
                console.log(JSON.stringify(data));
                this.setState({
                    projects: [
                        {
                            id: data.id,
                            title: data.title,
                            sourceLanguage: data.source_lang,
                            targetLanguage: data.target_lang,
                            lastSaved: data.timestamp,
                        },
                        {
                            id: 2,
                            title: "Homo Baraaus",
                            sourceLanguage: "EN",
                            targetLanguage: "TR",
                            lastSaved: "19/05/2017",
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

    render () {
        let { projects } = this.state;

        return (
            <div>
                <h1 className="center-wh" style={{paddingTop: 100}}>
                    Dashboard
                </h1>
                {projects.map(this.renderProjectListing.bind(this))}
            </div>
        );
    }
}

Dashboard.contextTypes = {
    router: PropTypes.object
};

export default Dashboard;
