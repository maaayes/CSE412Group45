--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Homebrew)
-- Dumped by pg_dump version 14.7 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: albums; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.albums (
    uad integer NOT NULL,
    name character varying,
    uid integer,
    doc date
);
INSERT INTO public.albums (uad, name, uid, doc)
VALUES
    (1, 'Volcanic Beats', 301, '2022-01-01');
    (2, 'Jungle Grooves', 302, '2022-01-15');
    (3, 'Savannah Suprise', 303, '2022-02-01');
    (4, 'Annies Rapids', 304, '2022-02-15');
    (5, 'Desert Mirage', 305, '2022-03-01');
    (6, 'Tinas Chicken Thighs', 306, '2022-03-15');
    (7, 'Mountainious Whispers', 307, '2022-04-01');
    (8, 'Various Animal Hearts', 308, '2022-04-15');
    (9, 'Ocean Odyssey 2022 Trip', 309, '2022-05-01');
    (10, 'Chile Pepper Fusion Resturant Design', 310, '2022-05-15');
    (11, 'Rhythm of the Rainforest on BlueRay', 311, '2022-06-01');
    (12, 'Prairie Pulse', 312, '2022-06-15');
    (13, 'MidJourney Suprise', 313, '2022-07-01');
    (14, 'Aurora Borealis Ballet', 314, '2022-07-15');
    (15, 'Wildfire Resturant Trip 2022', 315, '2022-08-01');

ALTER TABLE public.albums OWNER TO "rootUser";

--
-- Name: comments; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.comments (
    ucd integer NOT NULL,
    text character varying,
    userid integer,
    upd integer,
    dateleft date
);
INSERT INTO public.comments (ucd, text, userid, upd, dateleft)
VALUES
    (1, 'Love those cornfield races in middle America!', 301, 1630446325, '2022-01-02'),
    (2, 'The prairies are so peaceful, perfect for a Sunday drive.', 302, 1630446325, '2022-01-16'),
    (3, 'Just saw a dolphin while cruising along the coast!', 303, 1630446325, '2022-02-02'),
    (4, 'Nothing beats the freedom of a road trip in the heartland.', 304, 1630446325, '2022-02-16'),
    (5, 'The new Mustang is fast, but it still can''t outrun a cheetah!', 305, 1630446326, '2022-03-02'),
    (6, 'Did you know that the sea turtle can travel thousands of miles?', 306, 1630446326, '2022-03-16'),
    (7, 'I wish I had a submarine to explore the ocean depths.', 307, 1630446328, '2022-04-02'),
    (8, 'This weekend, I''ll be racing my Camaro at the local track!', 308, 1630446329, '2022-04-16'),
    (9, 'Route 66 still captures the spirit of middle America.', 309, 1630446325, '2022-05-02'),
    (10, 'Sharks are fascinating creatures, don''t you think?', 310, 1630446331, '2022-05-16'),
    (11, 'Taking a scenic drive through the Great Plains is amazing.', 311, 1630446325, '2022-06-02'),
    (12, 'Did you know that the octopus can change its color?', 312, 1630446325, '2022-06-16'),
    (13, 'The Corvette is an American classic, perfect for open roads.', 313, 1630446331, '2022-07-02'),
    (14, 'I love exploring small towns and local diners in middle America.', 314, 1630446332, '2022-07-16'),
    (15, 'Jellyfish are such mesmerizing creatures, don''t you agree?', 315, 1630446323, '2022-08-02');


ALTER TABLE public.comments OWNER TO "rootUser";

--
-- Name: friends; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.friends (
    userid integer NOT NULL,
    friend integer,
    friendshipdate date
);
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (1, 6, '2022-03-15');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (2, 9, '2022-01-20');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (3, 4, '2021-12-05'); #sample data says 3 3 but that wont work
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (4, 5, '2022-02-10');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (5, 10, '2021-11-08');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (6, 1, '2021-09-01');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (7, 6, '2022-04-01');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (8, 10, '2022-03-05');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (9, 7, '2021-10-15');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (10, 5, '2022-03-30');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (311, 8, '2022-02-25');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (314, 311, '2022-04-20');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (312, 3, '2021-11-30');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (5, 315, '2021-10-10');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (6, 311, '2022-03-01');

ALTER TABLE public.friends OWNER TO "rootUser";

--
-- Name: likes; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.likes (
    upd integer NOT NULL,
    userid integer,
    likecount integer
);

INSERT INTO public.likes (upd, userid, likecount) VALUES (10000, 1, 0);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10001, 1, 10);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10002, 2, 2);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10003, 2, 21);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10004, 3, 4);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10005, 5, 29);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10006, 5, 7);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10007, 5, 0);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10008, 7, 10);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10009, 8, 23);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10010 8, 47);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10011 9, 12);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10012, 13, 9);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10013, 14, 21);
INSERT INTO public.likes (upd, userid, likecount) VALUES (10014, 15, 4);
ALTER TABLE public.likes OWNER TO "rootUser";

--
-- Name: photos; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.photos (
    upd integer NOT NULL,
    uad integer,
    caption character varying,
    data character varying,
    filepath character varying
);
#change here from data to data containing date
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10000, 1, 'my fav trip', '2022-04-24', 'image1.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10001, 2, 'europe 2022', '2022-04-24', 'image2.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10002, 3, 'fav resturant', '2022-04-24', 'image3.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10003, 4, 'my friends', '2022-04-24', 'image4.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10004, 5, 'my family', '2022-04-24', 'image5.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10005, 6, 'extra photos', '2022-04-24', 'image6.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10006, 7, 'graduation event', '2022-04-24', 'image7.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10007, 8, 'wedding event', '2022-04-24', 'image8.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10008, 9, 'the beach', '2022-04-24', 'image9.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10009, 10, 'my fav photo', '2022-04-24', 'image10.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10010, 11, 'last summer was fun', '2022-04-24', 'image11.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10011, 12, 'thanksgiving w/family', '2022-04-24', 'image12.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10012, 13, 'financial savyness', '2022-04-24', 'image13.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10013, 14, 'older chickens for sale', '2022-04-24', 'image14.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (10014, 15, 'young grasshopper snacks', '2022-04-24', 'image15.png');


ALTER TABLE public.photos OWNER TO "rootUser";

--
-- Name: tags; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.tags (
    tag character varying NOT NULL,
    upd integer
);

INSERT INTO public.tags (tag, upd) VALUES ('trip', 10000);
INSERT INTO public.tags (tag, upd) VALUES ('fun', 10000);
INSERT INTO public.tags (tag, upd) VALUES ('favorite', 10002);
INSERT INTO public.tags (tag, upd) VALUES ('friends', 10003);
INSERT INTO public.tags (tag, upd) VALUES ('family', 10004);
INSERT INTO public.tags (tag, upd) VALUES ('yay', 10006);
INSERT INTO public.tags (tag, upd) VALUES ('congrats', 10006);
INSERT INTO public.tags (tag, upd) VALUES ('happy', 10007);
INSERT INTO public.tags (tag, upd) VALUES ('ocean', 10008);
INSERT INTO public.tags (tag, upd) VALUES ('favorite', 10009;
INSERT INTO public.tags (tag, upd) VALUES ('boston', 10010);
INSERT INTO public.tags (tag, upd) VALUES ('boston', 10011);
INSERT INTO public.tags (tag, upd) VALUES ('finance', 10012);
INSERT INTO public.tags (tag, upd) VALUES ('health', 10013);
INSERT INTO public.tags (tag, upd) VALUES ('politics', 10014);
INSERT INTO public.tags (tag, upd) VALUES ('keywest', 10015);

ALTER TABLE public.tags OWNER TO "rootUser";

--
-- Name: users; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.users (
    userid integer NOT NULL,
    fname character varying,
    lname character varying,
    email character varying,
    dob date,
    hometown character varying,
    gender character varying,
    password character varying,
    albumnum integer
    contribution_score integer
);

INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (1, 'John', 'Smith', 'jsmith@gmail.com', '2000-05-03', 'Phoenix', 'M', 'smith12', 0,0);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (2, 'Mary', 'James', 'mjames@gmail.com', '1998-11-21', 'Seattle', 'F', 'james34', 1,10);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (3, 'Noah', 'Miller', 'nmiller@gmail.com', '2001-02-14', 'Phoenix', 'M', 'miller56', 3,11);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (4, 'Olivia', 'Johnson', 'ojohnson@gmail.com', '2003-06-25', 'Springfield', 'F', 'john78', 1,12);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (5, 'Sam', 'Williams', 'swilliams@gmail.com', '2000-12-17', 'Franklin', 'M', 'will90', 0,13);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (6, 'Nicole', 'Wilson', 'nwilson@gmail.com', '2001-10-30', 'Madison', 'F', 'wilson22', 2,14);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (7, 'Sara', 'Miller', 'smiller@gmail.com', '1993-04-23', 'Oakland', 'F', 'mill35', 0,15);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (8, 'Mike', 'Jones', 'mjones@gmail.com', '2002-07-16', 'Denver', 'F', 'jones09', 1,27);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (9, 'Lisa', 'Davis', 'ldavis@gmail.com', '1997-03-24', 'Boston', 'F', 'davis23', 2,18);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (10, 'Liam', 'Brown', 'lbrown@gmail.com', '1999-10-25', 'Chicago', 'M', 'brown79', 1,19);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (311, 'Jay', 'Bloc', 'jbloc@asu.edu', '1998-09-30', 'Flagstaff', 'M', 'password11', 2,22)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (312, 'Kodak', 'Black', 'kblack@asu.edu', '1999-10-30', 'Oro Heights', 'M', 'password12', 2,33)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (313, 'Young', 'Thug', 'ythug@asu.edu', '1997-03-20', 'LA', 'M', 'password13', 2,4)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (314, 'Quavo', 'Migos', 'quavo@asu.edu', '1999-04-10', 'San Dimas', 'M', 'password14', 2,5)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (315, 'SHOW', 'GALANTIS', 'galantis@asu.edu', '1991-01-10', 'The Valley', 'M', 'password15', 2,6)
ALTER TABLE public.users OWNER TO "rootUser";

--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: rootUser
--

CREATE TABLE public.albums (
    userid integer not NULL

)
COPY public.albums (uad, name, uid, doc) FROM stdin;
\.


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.comments (ucd, text, userid, upd, dateleft) FROM stdin;
\.


--
-- Data for Name: friends; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.friends (userid, friend, friendshipdate) FROM stdin;
\.


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.likes (upd, userid, likecount) FROM stdin;
\.


--
-- Data for Name: photos; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.photos (upd, uad, caption, data, filepath) FROM stdin;
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.tags (tag, upd) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) FROM stdin;
\.


--
-- Name: albums albums_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pkey PRIMARY KEY (uad);


--
-- Name: albums albums_uid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_uid_key UNIQUE (uid);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (ucd);


--
-- Name: friends friends_friend_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT friends_friend_key UNIQUE (friend);


--
-- Name: friends friends_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT friends_pkey PRIMARY KEY (userid);


--
-- Name: likes likes_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (upd);


--
-- Name: likes likes_userid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_userid_key UNIQUE (userid);


--
-- Name: photos photos_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_pkey PRIMARY KEY (upd);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (tag);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- PostgreSQL database dump complete
--
