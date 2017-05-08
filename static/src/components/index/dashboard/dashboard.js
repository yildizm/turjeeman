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
        this.setState({
            projects: [
                {
                    id: 1,
                    title: "Baraa Stuff",
                    sourceLanguage: "AR",
                    targetLanguage: "TR",
                    lastSaved: "23/07/2016",
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
