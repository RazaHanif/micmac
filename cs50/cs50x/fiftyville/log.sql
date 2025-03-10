-- Keep a log of any SQL queries you execute as you solve the mystery.

-- STARTING INFO
-- the theft took place on July 28, 2021 and that it took place on Humphrey Street.

-- Get database layout
.schema

-- Getting some basic from the crime scene report

SELECT
  id,
  description
FROM
  crime_scene_reports
WHERE
  YEAR = '2021'
  AND MONTH = '07'
  AND DAY = '28'
  AND street = 'Humphrey Street';

/*
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time –
each of their interview transcripts mentions the bakery. */


-- Access the relavent interviews from the database, keyword bakery

SELECT
  id,
  name,
  transcript
FROM
  interviews
WHERE
  YEAR = '2021'
  AND MONTH = '07'
  AND DAY = '28'
  AND transcript LIKE '%bakery%';

-- Securtiy cameras from 10:15am - 10:25am will have escape car license
-- Theif withdrew money from ATM on Leggett Street before 10:15 am
-- Theif made a sub 1 min phone call, Accomplice made flight purchase at this time
-- Plan to take first flight out of Fiftyville on 07/29/2021

-- Find out FiftyVille airport code
SELECT
  *
FROM
  airports;

/*
| 1  | ORD          | O'Hare International Airport            | Chicago       |
| 2  | PEK          | Beijing Capital International Airport   | Beijing       |
| 3  | LAX          | Los Angeles International Airport       | Los Angeles   |
| 4  | LGA          | LaGuardia Airport                       | New York City |
| 5  | DFS          | Dallas/Fort Worth International Airport | Dallas        |
| 6  | BOS          | Logan International Airport             | Boston        |
| 7  | DXB          | Dubai International Airport             | Dubai         |
| 8  | CSF          | Fiftyville Regional Airport             | Fiftyville    |
| 9  | HND          | Tokyo International Airport             | Tokyo         |
| 10 | CDG          | Charles de Gaulle Airport               | Paris         |
| 11 | SFO          | San Francisco International Airport     | San Francisco |
| 12 | DEL          | Indira Gandhi International Airport     | Delhi         |
 */

--  Find all flights from Fiftyville on the following day (07/29/2021)

SELECT
  *
FROM
  flights
WHERE
  YEAR = '2021'
  AND MONTH = '07'
  AND DAY = '29'
  AND origin_airport_id = '8'
ORDER BY
  HOUR;

-- First flight that day left at 8:20 and went to NYC
-- Flight ID - 36

/*
Using all the info i have, find a suspect who
1 went to the atm that day
2 Left the bakery parking lot between 10:15 - 10:25
3 Made a sub 1 min outgoing call
4 left on flight 36
 */

SELECT DISTINCT
  people.id,
  people.name,
  people.license_plate,
  people.phone_number
FROM
  people
  JOIN phone_calls ON people.phone_number = phone_calls.caller
  JOIN bank_accounts ON people.id = bank_accounts.person_id
  JOIN passengers ON people.passport_number = passengers.passport_number
WHERE
  bank_accounts.account_number IN (
    SELECT
      account_number
    FROM
      atm_transactions
    WHERE
      YEAR = '2021'
      AND MONTH = '07'
      AND DAY = '28'
      AND atm_location = 'Leggett Street'
      AND transaction_type = 'withdraw'
  )
  AND people.license_plate IN (
    SELECT
      license_plate
    FROM
      bakery_security_logs
    WHERE
      YEAR = '2021'
      AND MONTH = '07'
      AND DAY = '28'
      AND HOUR = '10'
      AND MINUTE < '25'
  )
  AND people.phone_number IN (
    SELECT
      caller
    FROM
      phone_calls
    WHERE
      YEAR = '2021'
      AND MONTH = '07'
      AND DAY = '28'
      AND duration < '60'
  )
  AND people.passport_number IN (
    SELECT
      passport_number
    FROM
      passengers
    WHERE
      flight_id = '36'
  );

/*
SUSPECTS
BRUCE - 686048
 */

-- Check suspects call logs, see who they called
SELECT DISTINCT
  people.id,
  people.name,
  people.license_plate,
  people.phone_number
FROM
  people
  JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE
  people.phone_number IN (
    SELECT
      receiver
    FROM
      phone_calls
    WHERE
      YEAR = '2021'
      AND MONTH = '07'
      AND DAY = '28'
      AND duration < '60'
      AND caller = '(367) 555-5533'
  );

/*
ACCOMPLICE
ROBIN - 864400
 */

--  Just realized this is batman and robin lol