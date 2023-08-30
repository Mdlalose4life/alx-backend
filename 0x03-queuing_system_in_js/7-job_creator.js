#!/usr/bin/yarn dev
import { createQueue } from "kue";

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const queue = createQueue({name: 'push_notification_code_2'});

for (jobElem in jobs){
  const job = createQueue('push_notification_code_2', jobElem);

  job.on('enqueue', () => {
    console.log(`Notification job created: `, job.id);
    })
  job.on('completed', () => {
    console.log(`Notification job`, job.id, `completed`);
    })
  job.on('failed', (err) => {
    console.log(`Notification job`, job.err, `failed:` , err.message || err.toString());
    })
  job.on('progress', () => {
    console.log(`Notification job`, job.id ` ${process}% complete`);
    });
  job.save();
}