#!/usr/bin/yarn dev
import { createQueu } from 'kue'

const queue = createQueu();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${ phoneNumber },`, 
  `with message: ${ message }`
  );
};

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.phoneNumber, job.message);
    done();
});