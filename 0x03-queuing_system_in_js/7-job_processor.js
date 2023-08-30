#!/usr/bin/yarn dev
import { createQueue } from "kue";

blacklisted_numbers = ['4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done => {
  const total = 100;

})