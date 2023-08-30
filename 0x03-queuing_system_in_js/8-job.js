#!/usr/bin/yarn dev
import { Queue, Job } from "kue";

const createPushNotificationsJobs = (jobs, queue) =>{
  if (!(jobs instanceof Array)){
    throw new Error('Jobs is not an array');
  }
  for (let job_info in jobs) {
    const job = queue.create('push_notification_code_3', job_info)

    job.on('enqueue', () => {
        console.log('Notification job created:', job.id);
    })
    job.on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
    job.on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
    job.on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
    job.save();
  }
};

export default createPushNotificationsJobs;