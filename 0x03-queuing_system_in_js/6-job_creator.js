#!/usr/bin/yarn dev
import { createQueu } from 'kue'

const queue = createQueu({name: 'push_notification_code'});

const job = queue.create('push_notification_code',{
    phoneNumber: '0765142848',
    message: 'Account Created',
})

job.on('enqueue', () => {
    console.log('Notification job created:', job.id);
})
job.on('completed', () => {
    console.log('Notification job completed');
})
job.on('job_failed', () => {
    console.log('Notification job failed');
})
job.save();