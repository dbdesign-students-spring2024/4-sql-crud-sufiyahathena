# SQL CRUD

# Part 1: Restaurants

## SQL Code to Create Tables
code also found in create_tables.sql

CREATE TABLE restaurants (
    RestaurantID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Category TEXT,
    PriceTier TEXT,
    Neighborhood TEXT,
    OpeningHours TEXT,
    ClosingHours TEXT,
    AverageRating REAL,
    GoodForKids BOOLEAN
);

CREATE TABLE reviews (
    ReviewID INTEGER PRIMARY KEY,
    RestaurantID INTEGER,
    Rating INTEGER,
    Comment TEXT,
    Date TEXT,
    FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID)
);

## Code written in Terminal:
cd /Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena
sqlite3 MyDatabase.db
sqlite> DROP TABLE IF EXISTS restaurants;
sqlite> .mode csv
sqlite> .import restaurants.csv restaurants


## 1. Find all cheap restaurants in a particular neighborhood = Chelsea
sqlite> SELECT * FROM restaurants
WHERE PriceTier = 'Cheap' AND Neighborhood = 'Chelsea';

## Output: 
2,Skinix,Mediterranean,Cheap,Chelsea,7:57,7:28,3,false
9,Ntag,Italian,Cheap,Chelsea,21:39,22:19,3,true
16,Agivu,Greek,Cheap,Chelsea,23:48,23:23,2,false
25,Demimbu,Indian,Cheap,Chelsea,9:36,6:03,2,true
26,Blogtags,Arabic,Cheap,Chelsea,18:10,4:14,4,false
29,Zooxo,Italian,Cheap,Chelsea,6:12,15:00,4,true
36,Jetwire,Italian,Cheap,Chelsea,5:46,14:04,3,true
51,Yabox,Mexican,Cheap,Chelsea,23:24,20:28,3,true
52,Tekfly,Mexican,Cheap,Chelsea,15:05,0:17,5,false
56,Yakidoo,Arabic,Cheap,Chelsea,8:33,2:41,1,true
124,Topiczoom,Mediterranean,Cheap,Chelsea,14:05,2:13,2,true
130,Kimia,Chinese,Cheap,Chelsea,17:53,2:45,5,false
159,Centimia,Arabic,Cheap,Chelsea,6:08,13:16,1,false
168,Talane,Mediterranean,Cheap,Chelsea,3:16,10:11,1,false
179,Quatz,Mediterranean,Cheap,Chelsea,16:54,7:06,1,false
183,Plambee,Chinese,Cheap,Chelsea,11:05,5:53,5,true
199,Jaxspan,Czech,Cheap,Chelsea,21:15,11:48,4,true
267,Camido,Greek,Cheap,Chelsea,0:15,18:55,3,true
273,Trilia,Greek,Cheap,Chelsea,12:31,5:06,5,true
274,Fadeo,Greek,Cheap,Chelsea,9:17,5:59,4,true
276,Jabberbean,Greek,Cheap,Chelsea,8:26,2:46,1,false
283,Nlounge,Mediterranean,Cheap,Chelsea,12:49,17:11,1,true
306,Tagpad,Mexican,Cheap,Chelsea,13:53,18:49,2,true
314,Riffwire,Mediterranean,Cheap,Chelsea,22:15,5:26,3,false
334,Gabcube,Chinese,Cheap,Chelsea,2:05,6:20,1,false
348,Skajo,Czech,Cheap,Chelsea,10:02,13:47,3,false
351,Feednation,Chinese,Cheap,Chelsea,17:55,19:21,3,false
408,Twinte,Greek,Cheap,Chelsea,1:34,16:02,2,false
438,Jamia,Chinese,Cheap,Chelsea,13:54,16:03,2,false
454,Plajo,Indian,Cheap,Chelsea,0:49,2:10,5,false
492,Twimbo,Czech,Cheap,Chelsea,12:57,10:33,2,true
529,Topdrive,Chinese,Cheap,Chelsea,2:37,0:30,3,true
543,Jatri,Thai,Cheap,Chelsea,14:22,7:04,4,true
577,Gigashots,Italian,Cheap,Chelsea,13:02,1:56,1,false
582,Topicware,Czech,Cheap,Chelsea,10:11,0:36,3,false
619,DabZ,Arabic,Cheap,Chelsea,3:07,17:39,3,false
625,Eabox,Thai,Cheap,Chelsea,18:25,9:38,5,false
709,Dabjam,Chinese,Cheap,Chelsea,22:49,23:09,5,true
745,Realpoint,Thai,Cheap,Chelsea,20:41,5:51,5,true
767,Oba,Thai,Cheap,Chelsea,15:54,23:15,4,false
800,Voonte,Greek,Cheap,Chelsea,10:23,11:06,5,false
805,Yadel,Mexican,Cheap,Chelsea,22:18,20:51,3,true
833,Gevee,Mexican,Cheap,Chelsea,16:49,2:38,2,false
858,Divavu,Mexican,Cheap,Chelsea,0:08,20:24,5,true
933,Yoveo,Thai,Cheap,Chelsea,4:27,22:40,1,false
950,Voonder,Chinese,Cheap,Chelsea,1:08,16:54,3,false
976,Skiba,Indian,Cheap,Chelsea,12:36,9:43,1,true
1000,Voolith,Indian,Cheap,Chelsea,17:21,18:30,5,false

## 2. Find all restaurants in a particular genre with 3 stars or more, ordered by the number of stars in descending order = Italian
SELECT * FROM restaurants
WHERE Category = 'Italian' AND AverageRating >= 3
ORDER BY AverageRating DESC;

## Output
8,Avaveo,Italian,Average,"Upper East Side",21:25,10:32,5,false
27,Skipfire,Italian,Cheap,Soho,20:03,7:23,5,false
88,Blogpad,Italian,Cheap,"Hudson Yards",14:52,6:32,5,false
109,Meetz,Italian,Average,"Hudson Yards",18:16,23:41,5,false
133,Roombo,Italian,Average,"Hudson Yards",0:42,14:59,5,true
154,Topicstorm,Italian,Expensive,Harlem,7:56,22:16,5,true
180,Jetpulse,Italian,Expensive,Chelsea,7:43,17:19,5,true
223,Kwinu,Italian,Average,Soho,22:24,17:25,5,true
233,Meevee,Italian,Average,"Hudson Yards",19:52,7:58,5,false
310,Twitternation,Italian,Average,"East Village",8:25,10:26,5,true
430,Voolia,Italian,Average,"Upper East Side",0:23,14:23,5,true
452,Ozu,Italian,Cheap,Harlem,18:25,16:14,5,false
506,Blogspan,Italian,Cheap,Harlem,0:21,19:40,5,false
531,Quamba,Italian,Expensive,Soho,13:50,10:07,5,false
569,Skimia,Italian,Average,Soho,10:52,15:33,5,false
573,Topdrive,Italian,Cheap,"Financial District",5:12,17:27,5,true
624,Jaloo,Italian,Expensive,"Upper East Side",18:16,4:25,5,true
647,Fatz,Italian,Expensive,Harlem,2:09,20:11,5,false
665,Edgeclub,Italian,Expensive,Soho,19:14,3:59,5,false
742,Flashspan,Italian,Cheap,"East Village",22:59,5:41,5,false
770,Feedspan,Italian,Cheap,"East Village",18:37,6:59,5,false
779,Twinte,Italian,Average,Soho,12:19,0:37,5,true
781,Trunyx,Italian,Cheap,Harlem,22:54,4:47,5,true
785,Voonte,Italian,Expensive,Soho,12:20,16:25,5,true
803,Skippad,Italian,Average,Soho,8:44,22:52,5,false
807,Mynte,Italian,Expensive,Soho,13:26,8:00,5,true
897,Fivechat,Italian,Average,Soho,23:42,5:09,5,true
899,Rhynoodle,Italian,Average,Soho,22:08,6:26,5,false
19,Aibox,Italian,Average,"East Village",15:45,14:53,4,true
29,Zooxo,Italian,Cheap,Chelsea,6:12,15:00,4,true
35,Jabbersphere,Italian,Expensive,"East Village",0:22,15:31,4,true
57,Jabberbean,Italian,Cheap,"Upper East Side",4:21,22:52,4,true
66,Fivebridge,Italian,Average,Harlem,8:30,21:13,4,true
84,Kayveo,Italian,Average,Soho,14:55,3:49,4,true
119,Camido,Italian,Expensive,"Hudson Yards",21:11,22:40,4,false
152,Rhynyx,Italian,Average,"Upper East Side",11:04,12:51,4,true
156,Ooba,Italian,Expensive,Soho,10:08,14:15,4,false
186,Skinix,Italian,Average,Chelsea,15:45,7:05,4,true
189,Youbridge,Italian,Average,"Hudson Yards",1:42,6:40,4,true
293,Pixope,Italian,Expensive,"Financial District",12:03,5:41,4,true
297,Devbug,Italian,Cheap,"Hudson Yards",15:40,1:49,4,false
331,Reallinks,Italian,Average,Soho,12:42,3:35,4,false
396,Feedfish,Italian,Average,"Hudson Yards",3:09,18:44,4,true
402,Twimm,Italian,Expensive,"Upper East Side",19:11,14:26,4,false
539,Wordtune,Italian,Average,Harlem,5:21,12:19,4,true
578,Blogpad,Italian,Cheap,"Upper East Side",8:18,9:39,4,false
621,Zoonoodle,Italian,Expensive,"Hudson Yards",14:02,7:07,4,true
677,Dabjam,Italian,Cheap,Harlem,18:10,8:00,4,true
736,Aimbu,Italian,Cheap,"Hudson Yards",11:13,4:59,4,true
791,Skyvu,Italian,Average,"East Village",4:30,1:53,4,true
792,Fivechat,Italian,Expensive,"Hudson Yards",7:47,11:01,4,true
798,Tambee,Italian,Cheap,"East Village",10:26,20:36,4,false
809,Snaptags,Italian,Cheap,Soho,10:27,0:56,4,false
841,Pixonyx,Italian,Cheap,Harlem,23:53,11:06,4,true
849,Skinder,Italian,Expensive,"East Village",20:06,8:49,4,false
977,Bluezoom,Italian,Average,"Financial District",2:09,21:44,4,false
9,Ntag,Italian,Cheap,Chelsea,21:39,22:19,3,true
36,Jetwire,Italian,Cheap,Chelsea,5:46,14:04,3,true
59,Realfire,Italian,Expensive,"East Village",13:32,3:43,3,false
169,Yodoo,Italian,Average,Chelsea,6:16,9:03,3,false
195,Youopia,Italian,Average,"Financial District",3:07,13:07,3,false
210,Blogspan,Italian,Average,Harlem,4:30,0:50,3,false
228,Gabtype,Italian,Expensive,Harlem,23:48,1:06,3,true
250,Yambee,Italian,Cheap,"Hudson Yards",15:18,9:33,3,true
265,Edgepulse,Italian,Expensive,"Hudson Yards",9:27,1:27,3,true
327,Dabfeed,Italian,Average,Soho,17:11,2:20,3,true
346,Flashdog,Italian,Expensive,Chelsea,3:05,7:20,3,false
421,Brightdog,Italian,Expensive,"Hudson Yards",3:13,20:56,3,false
456,Realbridge,Italian,Expensive,"Financial District",23:47,18:05,3,true
475,Browsetype,Italian,Average,"Financial District",4:29,17:29,3,true
575,Vidoo,Italian,Expensive,"Upper East Side",4:25,0:01,3,false
576,Gevee,Italian,Average,Harlem,19:12,9:38,3,false
590,Photobug,Italian,Average,"East Village",12:21,14:21,3,false
608,Zoombeat,Italian,Expensive,"Upper East Side",11:26,9:11,3,false
631,Linktype,Italian,Average,Harlem,3:19,23:13,3,true
656,Divavu,Italian,Expensive,Harlem,14:33,2:00,3,true
684,Thoughtworks,Italian,Average,"Financial District",11:52,14:39,3,false
707,Jabbertype,Italian,Average,"Financial District",8:14,2:27,3,false
748,Izio,Italian,Cheap,"Upper East Side",0:26,21:43,3,false
812,Rhyloo,Italian,Cheap,Harlem,13:19,7:49,3,false
822,Eadel,Italian,Expensive,Chelsea,10:55,11:15,3,true
827,Livefish,Italian,Expensive,"Financial District",22:22,4:04,3,true
868,Jayo,Italian,Expensive,Harlem,1:37,11:17,3,false
884,Blogtags,Italian,Average,"Upper East Side",17:53,18:45,3,false
929,Babbleopia,Italian,Expensive,"Financial District",19:21,18:20,3,true
992,Riffpath,Italian,Average,Harlem,2:52,18:41,3,true

## Find all restaurants that are open now
 SELECT * FROM restaurants
WHERE strftime('%H:%M', 'now', 'localtime') BETWEEN OpeningHours AND ClosingHours;

## Output
14,Izio,Indian,Average,Soho,13:03,15:35,3,false
15,Brightbean,Chinese,Average,"East Village",0:16,3:14,5,false
31,Oodoo,Indian,Expensive,"Hudson Yards",13:40,23:19,1,true
32,Wikizz,Thai,Cheap,"East Village",13:33,18:35,5,true
35,Jabbersphere,Italian,Expensive,"East Village",0:22,15:31,4,true
38,Rhyloo,Indian,Average,"Upper East Side",12:45,8:24,4,false
46,LiveZ,Thai,Average,"Financial District",10:04,6:39,1,false
54,Topicstorm,Czech,Expensive,Harlem,12:27,7:46,1,true
55,Trupe,Thai,Cheap,"Hudson Yards",10:26,21:23,4,false
59,Realfire,Italian,Expensive,"East Village",13:32,3:43,3,false
63,Tekfly,Arabic,Cheap,Soho,0:39,3:33,2,false
70,Pixonyx,Indian,Expensive,Soho,11:12,20:13,3,false
71,Tazz,Greek,Cheap,"East Village",0:00,17:28,4,false
72,Kanoodle,Mediterranean,Expensive,"Hudson Yards",0:19,15:09,1,true
78,Roodel,Mediterranean,Expensive,Harlem,14:05,1:47,4,false
81,Eire,Mediterranean,Cheap,"Hudson Yards",11:44,3:05,1,true
86,Podcat,Arabic,Average,"Financial District",11:54,7:40,3,true
97,Roombo,Mexican,Cheap,"East Village",13:11,23:01,1,true
106,Livepath,Arabic,Expensive,Soho,0:49,17:36,1,true
112,Quire,Greek,Cheap,"East Village",13:31,5:48,2,false
118,Ailane,Mediterranean,Cheap,Harlem,11:54,20:42,2,false
120,Aibox,Chinese,Expensive,"Upper East Side",14:05,15:59,1,true
124,Topiczoom,Mediterranean,Cheap,Chelsea,14:05,2:13,2,true
125,Edgeclub,Greek,Cheap,"Financial District",10:29,19:44,3,true
132,Youspan,Czech,Cheap,"Hudson Yards",10:07,5:39,4,true
133,Roombo,Italian,Average,"Hudson Yards",0:42,14:59,5,true
149,Npath,Czech,Average,"Financial District",0:31,17:27,4,true
153,Mita,Chinese,Expensive,"Hudson Yards",10:06,18:31,5,false
156,Ooba,Italian,Expensive,Soho,10:08,14:15,4,false
166,Zoombox,Chinese,Cheap,"Upper East Side",0:56,1:00,3,false
171,Wordtune,Mediterranean,Cheap,"Upper East Side",0:16,16:26,1,true
173,Skajo,Thai,Average,"Hudson Yards",12:28,17:02,4,false
176,Photospace,Mediterranean,Cheap,Harlem,13:28,22:14,3,false
183,Plambee,Chinese,Cheap,Chelsea,11:05,5:53,5,true
184,Twitterworks,Greek,Expensive,"Hudson Yards",0:07,5:40,3,true
192,Zava,Mexican,Average,"Hudson Yards",0:21,2:48,4,true
202,Jetpulse,Indian,Expensive,"Financial District",10:30,9:29,3,false
211,Cogidoo,Czech,Average,"Financial District",12:48,17:27,2,true
218,Yakijo,Italian,Average,Chelsea,0:14,16:48,1,false
222,Tekfly,Chinese,Expensive,Soho,12:33,14:25,1,true
226,Jabberbean,Thai,Average,"Hudson Yards",13:06,5:28,1,false
246,Twitterwire,Indian,Expensive,"East Village",12:57,22:24,1,true
251,Teklist,Mexican,Cheap,Harlem,12:27,2:05,2,true
252,Centizu,Czech,Expensive,Harlem,0:02,17:51,4,true
254,Flashdog,Arabic,Cheap,Harlem,13:13,8:13,2,true
261,Lajo,Mediterranean,Expensive,Harlem,11:43,18:37,3,true
263,Kwideo,Greek,Expensive,"East Village",11:49,6:29,5,false
267,Camido,Greek,Cheap,Chelsea,0:15,18:55,3,true
271,Babbleblab,Thai,Expensive,"Hudson Yards",13:16,3:19,3,false
273,Trilia,Greek,Cheap,Chelsea,12:31,5:06,5,true
283,Nlounge,Mediterranean,Cheap,Chelsea,12:49,17:11,1,true
293,Pixope,Italian,Expensive,"Financial District",12:03,5:41,4,true
306,Tagpad,Mexican,Cheap,Chelsea,13:53,18:49,2,true
311,Twinder,Mexican,Average,"Upper East Side",11:26,19:11,1,false
320,Devify,Arabic,Cheap,"Hudson Yards",0:38,6:26,4,true
322,Npath,Thai,Expensive,"Hudson Yards",11:36,7:06,1,true
331,Reallinks,Italian,Average,Soho,12:42,3:35,4,false
332,Vitz,Czech,Cheap,"Financial District",11:00,21:47,2,false
333,Divape,Mexican,Expensive,"Upper East Side",10:08,6:43,4,true
335,Voonder,Arabic,Average,Harlem,13:55,21:33,3,true
353,Buzzshare,Chinese,Expensive,Chelsea,14:03,19:07,5,false
358,Skilith,Mexican,Average,Harlem,11:52,22:58,1,false
362,Eare,Greek,Cheap,Harlem,11:28,2:46,5,false
366,Livetube,Indian,Average,Chelsea,13:52,21:35,2,true
388,Mynte,Indian,Average,Chelsea,11:34,20:04,3,false
390,Gigazoom,Mexican,Expensive,"Financial District",12:03,14:18,4,true
406,Kwimbee,Czech,Expensive,Soho,12:22,1:08,4,true
415,Wikido,Indian,Cheap,"Upper East Side",12:11,19:25,4,true
426,Mycat,Mexican,Cheap,Soho,12:07,1:46,1,false
429,Zoozzy,Thai,Expensive,Harlem,11:52,8:33,1,true
430,Voolia,Italian,Average,"Upper East Side",0:23,14:23,5,true
432,Shuffletag,Chinese,Cheap,"Upper East Side",10:28,7:48,4,false
436,Feedspan,Chinese,Average,"Financial District",13:52,21:10,2,false
438,Jamia,Chinese,Cheap,Chelsea,13:54,16:03,2,false
445,Tagcat,Chinese,Expensive,Chelsea,10:19,1:05,4,false
450,Kayveo,Thai,Cheap,Harlem,0:01,8:21,4,true
454,Plajo,Indian,Cheap,Chelsea,0:49,2:10,5,false
472,Trilith,Arabic,Cheap,"East Village",0:29,23:37,3,false
474,Dynabox,Chinese,Average,"Hudson Yards",0:51,9:13,2,true
477,Meevee,Mexican,Expensive,"Financial District",12:19,9:37,2,false
479,Gabvine,Chinese,Cheap,Harlem,11:04,9:27,3,true
488,Skibox,Czech,Average,"Upper East Side",0:06,3:25,4,false
500,Flipopia,Chinese,Expensive,"East Village",11:04,14:26,3,true
504,Yakidoo,Mexican,Cheap,"East Village",13:46,7:47,5,false
506,Blogspan,Italian,Cheap,Harlem,0:21,19:40,5,false
508,Plambee,Indian,Cheap,"Hudson Yards",13:39,19:53,1,false
514,Innotype,Arabic,Expensive,"Financial District",0:02,23:22,4,false
522,InnoZ,Mexican,Expensive,"East Village",0:23,16:45,1,false
526,Bubbletube,Greek,Cheap,"East Village",12:49,19:18,2,false
528,Ntag,Chinese,Average,Chelsea,0:37,9:49,4,true
534,Cogidoo,Mediterranean,Average,"Upper East Side",13:54,4:15,1,true
541,Riffwire,Chinese,Expensive,Chelsea,11:26,16:12,3,false
542,Browsecat,Arabic,Cheap,"East Village",10:12,16:27,5,true
546,Jazzy,Mexican,Cheap,Soho,12:20,6:55,4,true
549,Babblestorm,Thai,Average,"East Village",0:51,22:14,1,false
552,Kazu,Thai,Expensive,"Hudson Yards",13:20,1:42,4,false
558,Trudoo,Italian,Expensive,"Financial District",12:16,17:03,2,false
560,Edgewire,Indian,Average,"Financial District",0:08,18:37,1,false
561,Trilia,Indian,Expensive,Harlem,0:40,14:24,4,true
562,Blogtag,Czech,Cheap,"Financial District",12:34,18:36,3,false
565,Skyba,Greek,Average,"East Village",10:44,2:52,4,false
569,Skimia,Italian,Average,Soho,10:52,15:33,5,false
577,Gigashots,Italian,Cheap,Chelsea,13:02,1:56,1,false
579,Blogtags,Thai,Cheap,"Hudson Yards",11:46,22:49,1,true
586,Demizz,Mexican,Average,"East Village",10:52,6:41,5,true
589,Mydeo,Greek,Expensive,Harlem,10:04,9:30,1,true
590,Photobug,Italian,Average,"East Village",12:21,14:21,3,false
591,Centidel,Arabic,Expensive,"East Village",13:14,2:54,3,true
604,Realfire,Mexican,Cheap,"Upper East Side",11:03,18:30,5,true
608,Zoombeat,Italian,Expensive,"Upper East Side",11:26,9:11,3,false
620,Avamm,Thai,Average,"Financial District",13:18,21:34,2,true
621,Zoonoodle,Italian,Expensive,"Hudson Yards",14:02,7:07,4,true
645,Skyble,Indian,Cheap,"Upper East Side",12:16,23:08,2,true
652,Browsebug,Chinese,Cheap,"Financial District",12:19,14:42,4,false
669,Buzzbean,Czech,Average,Harlem,10:09,16:57,2,false
678,Omba,Mediterranean,Average,Soho,12:22,15:30,4,true
684,Thoughtworks,Italian,Average,"Financial District",11:52,14:39,3,false
689,Dabfeed,Mediterranean,Expensive,"East Village",10:55,8:42,1,true
694,Plajo,Indian,Average,"East Village",11:41,23:31,5,false
695,Fanoodle,Thai,Average,Chelsea,13:13,16:46,5,false
696,Yadel,Indian,Expensive,"Financial District",13:58,20:53,2,true
697,JumpXS,Thai,Expensive,"East Village",13:57,7:43,2,true
699,Thoughtsphere,Thai,Cheap,"Financial District",10:12,16:00,5,false
700,Jabbersphere,Chinese,Cheap,"Upper East Side",11:58,17:20,1,true
706,Oba,Greek,Cheap,"Hudson Yards",13:37,22:40,2,false
711,Gigaclub,Mexican,Cheap,"East Village",13:01,3:53,4,false
712,Geba,Thai,Cheap,"East Village",0:05,9:54,5,false
713,Eadel,Czech,Average,"East Village",12:14,7:19,4,false
719,Bubbletube,Thai,Expensive,"Financial District",11:45,1:38,4,true
721,DabZ,Thai,Cheap,Harlem,0:10,23:46,2,false
722,Feedmix,Thai,Expensive,Harlem,10:52,22:17,3,true
723,Eidel,Indian,Expensive,Harlem,13:29,4:58,1,true
729,Pixope,Mediterranean,Average,"Upper East Side",12:09,3:37,2,false
732,Topiczoom,Mexican,Cheap,Soho,12:32,22:56,3,false
734,Dabshots,Mexican,Cheap,"East Village",10:20,17:34,4,false
735,Shuffletag,Indian,Expensive,"Financial District",10:01,6:17,4,true
736,Aimbu,Italian,Cheap,"Hudson Yards",11:13,4:59,4,true
738,Devcast,Czech,Cheap,Harlem,12:59,8:20,3,false
748,Izio,Italian,Cheap,"Upper East Side",0:26,21:43,3,false
754,Wikizz,Italian,Expensive,"Hudson Yards",10:01,14:35,1,false
764,Katz,Arabic,Expensive,"East Village",11:43,16:48,4,false
765,Meevee,Arabic,Expensive,Soho,13:08,6:35,4,false
780,Rhycero,Mexican,Average,Soho,11:01,15:15,1,true
782,Divavu,Greek,Cheap,"Financial District",12:55,17:41,1,false
784,Trupe,Chinese,Average,"Financial District",12:32,5:51,4,true
785,Voonte,Italian,Expensive,Soho,12:20,16:25,5,true
788,Bluezoom,Chinese,Average,"Hudson Yards",10:27,20:35,4,false
798,Tambee,Italian,Cheap,"East Village",10:26,20:36,4,false
799,Youspan,Czech,Expensive,Chelsea,0:23,3:26,5,true
807,Mynte,Italian,Expensive,Soho,13:26,8:00,5,true
812,Rhyloo,Italian,Cheap,Harlem,13:19,7:49,3,false
835,Abatz,Greek,Cheap,"Upper East Side",11:24,7:16,2,true
840,Edgepulse,Czech,Average,Harlem,10:50,16:04,4,true
845,Zoombeat,Mexican,Expensive,Harlem,0:04,20:51,3,false
852,Bluezoom,Indian,Average,Harlem,10:12,4:08,1,false
858,Divavu,Mexican,Cheap,Chelsea,0:08,20:24,5,true
860,Voonte,Greek,Cheap,"East Village",12:26,4:56,2,false
861,Kwideo,Greek,Average,"Financial District",13:41,3:03,5,true
864,Camido,Greek,Cheap,"East Village",10:34,8:30,2,true
885,Tagfeed,Mexican,Expensive,Harlem,12:02,17:25,1,false
903,Podcat,Mexican,Expensive,"Hudson Yards",13:33,23:10,3,false
904,Rhyloo,Arabic,Expensive,Soho,12:13,3:12,4,true
905,Trudeo,Chinese,Average,Harlem,0:55,19:36,3,false
915,Pixoboo,Thai,Expensive,Soho,12:13,16:53,1,true
920,Yamia,Mexican,Cheap,"East Village",0:44,5:31,5,true
924,Tagtune,Mediterranean,Average,Soho,12:34,22:49,3,true
928,Trunyx,Thai,Expensive,"East Village",12:54,15:08,3,false
932,Brightdog,Indian,Cheap,"Financial District",11:48,14:18,2,true
943,Oloo,Czech,Expensive,Harlem,0:00,4:12,1,false
947,Reallinks,Thai,Cheap,"Hudson Yards",10:54,15:25,5,true
967,Tagopia,Czech,Cheap,Harlem,11:34,16:18,1,true
970,Riffpath,Mediterranean,Average,Harlem,12:37,5:02,2,true
971,Youfeed,Greek,Average,Harlem,0:57,17:36,1,true
973,Vipe,Thai,Expensive,"Hudson Yards",13:51,1:20,5,true
976,Skiba,Indian,Cheap,Chelsea,12:36,9:43,1,true
980,Pixope,Chinese,Cheap,"Hudson Yards",12:12,15:00,4,false
982,Digitube,Czech,Expensive,"East Village",13:46,20:03,4,false
985,Eadel,Italian,Expensive,Harlem,0:36,17:06,1,true

## 4. Leave a review for a restaurant = RestaurantID 1
INSERT INTO reviews (RestaurantID, Rating, Comment, Date)
VALUES (1, 5, 'Excellent service and food!', '2024-03-12');

## Output
SELECT * FROM reviews WHERE RestaurantID = 1;

## 5. Delete all restaurants that are not good for kids
DELETE FROM restaurants
WHERE GoodForKids = 'false';

## Output
SELECT * FROM restaurants WHERE GoodForKids = 'false';
no rows indicates there are no restaurants

## 6. Find the number of restaurants in each NYC neighborhood
SELECT Neighborhood, COUNT(*) AS NumberOfRestaurants
FROM restaurants
GROUP BY Neighborhood;

## Output
Chelsea,64
"East Village",71
"Financial District",70
Harlem,93
"Hudson Yards",73
Soho,76
"Upper East Side",70

# Part 2: Social Media

## SQL Code to Create Tables
CREATE TABLE users (
    UserID INTEGER PRIMARY KEY,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    Handle TEXT NOT NULL
);

CREATE TABLE posts (
    PostID INTEGER PRIMARY KEY,
    UserID INTEGER,
    PostType TEXT NOT NULL,
    Content TEXT NOT NULL,
    RecipientID INTEGER,
    Visible BOOLEAN NOT NULL,
    CreationTime TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES users(UserID),
    FOREIGN KEY (RecipientID) REFERENCES users(UserID)
);

## Code written in Terminal:
Python Code to merge cvs files in merge_csv.py
'''
Python code:
import pandas as pd

messages_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/messages.csv'
stories_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/stories.csv'
merged_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/posts.csv'

messages_df = pd.read_csv(messages_csv_path)
stories_df = pd.read_csv(stories_csv_path)

stories_df['RecipientID'] = None
messages_df['Visible'] = True
stories_df['Visible'] = True

(Since stories are visible for 24 hours and messages are visible only once - simulate this by setting all to true)

posts_df = pd.concat([messages_df, stories_df], ignore_index=True)

posts_df.to_csv(merged_csv_path, index=False)

print(f'Merged posts saved to {merged_csv_path}')
'''

cd /Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/
python merge_csv.py

cd /Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena
sqlite3 MyDatabase.db
sqlite> .mode csv



