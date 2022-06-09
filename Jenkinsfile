#!/usr/bin/env groovy
import groovy.json.JsonOutput

node ('master') {
    
    def gitBranch = (params.git_branch_name) ?: 'master'
    def username = 'test'
    def password = 'test'

    stage('GitCheckoutRepo') {
      withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'GHE_API_TOKEN',
                      usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
        checkout scm
        dir('zsec-alerting-framework') {
          git branch: "${gitBranch}",
              credentialsId: 'GHE_API_TOKEN',
              url: 'https://git.zias.io/security/webapp.git'
        }
      }
    }
    
    environment {
		
              BUILDVERSION = sh(returnStdout: true, script: 'date +%H%M%S').trim()
	       //Use Pipeline Utility Steps plugin to read information from pom.xml into env variables
    	      IMAGE = readMavenPom().getArtifactId()
              VERSION = readMavenPom().getVersion()
	     
	     
    }

    stage ('Python Setup') {
      dir ("${env.WORKSPACE}") {
        sh "pip3 install --user virtualenv"
        sh "python3 -m virtualenv venv"
        sh "source venv/bin/activate"
        sh "pip3 install --user --quiet --upgrade pip"
        sh "pip3 install --user --quiet ansible==2.4.3.0 awscli boto six xmltodict requests paramiko testinfra==1.10.1 boto3"       
      }
    }
    
  }
