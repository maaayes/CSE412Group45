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

INSERT INTO public.albums (uad, name, uid, doc) VALUES (1, 'Volcano Beats', 101, '2022-01-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (2, 'Jungle Grooves', 102, '2022-01-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (3, 'Savannah Sunrise', 103, '2022-02-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (4, 'Raging Rapids', 104, '2022-02-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (5, 'Desert Mirage', 105, '2022-03-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (6, 'Tropical Thunder', 106, '2022-03-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (7, 'Mountain Whispers', 107, '2022-04-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (8, 'Lionheart', 108, '2022-04-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (9, 'Ocean Odyssey', 109, '2022-05-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (10, 'Chile Pepper Fusion', 110, '2022-05-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (11, 'Rhythm of the Rainforest', 111, '2022-06-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (12, 'Prairie Pulse', 112, '2022-06-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (13, 'Celestial Safari', 113, '2022-07-01');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (14, 'Aurora Borealis Ballet', 114, '2022-07-15');
INSERT INTO public.albums (uad, name, uid, doc) VALUES (15, 'Wildfire Waltz', 115, '2022-08-01');

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

INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (1, 'Love those cornfield races in middle America!', 201, 1, '2022-01-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (2, 'The prairies are so peaceful, perfect for a Sunday drive.', 202, 2, '2022-01-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (3, 'Just saw a dolphin while cruising along the coast!', 203, 3, '2022-02-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (4, 'Nothing beats the freedom of a road trip in the heartland.', 204, 4, '2022-02-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (5, 'The new Mustang is fast, but it still can''t outrun a cheetah!', 205, 5, '2022-03-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (6, 'Did you know that the sea turtle can travel thousands of miles?', 206, 6, '2022-03-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (7, 'I wish I had a submarine to explore the ocean depths.', 207, 7, '2022-04-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (8, 'This weekend, I''ll be racing my Camaro at the local track!', 208, 8, '2022-04-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (9, 'Route 66 still captures the spirit of middle America.', 209, 9, '2022-05-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (10, 'Sharks are fascinating creatures, don''t you think?', 210, 10, '2022-05-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (11, 'Taking a scenic drive through the Great Plains is amazing.', 211, 11, '2022-06-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (12, 'Did you know that the octopus can change its color?', 212, 12, '2022-06-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (13, 'The Corvette is an American classic, perfect for open roads.', 213, 13, '2022-07-02');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (14, 'I love exploring small towns and local diners in middle America.', 214, 14, '2022-07-16');
INSERT INTO public.comments (ucd, text, userid, upd, dateleft) VALUES (15, 'Jellyfish are such mesmerizing creatures, don''t you agree?', 215, 15, '2022-08-02');

ALTER TABLE public.comments OWNER TO "rootUser";

--
-- Name: friends; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.friends (
    userid integer NOT NULL,
    friend integer,
    friendshipdate date
);
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (301, 302, '2022-03-15');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (301, 305, '2022-01-20');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (301, 311, '2021-12-05');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (302, 304, '2022-02-10');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (302, 309, '2021-11-08');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (302, 312, '2021-09-01');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (303, 307, '2022-04-01');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (303, 315, '2022-03-05');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (303, 311, '2021-10-15');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (304, 309, '2022-03-30');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (304, 312, '2022-02-25');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (305, 309, '2022-04-20');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (305, 313, '2021-11-30');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (305, 315, '2021-10-10');
INSERT INTO public.friends (userid, friend, friendshipdate) VALUES (306, 311, '2022-03-01');

ALTER TABLE public.friends OWNER TO "rootUser";

--
-- Name: likes; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.likes (
    upd integer NOT NULL,
    userid integer,
    likecount integer
);

INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446325, 1, 10);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446326, 2, 5);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446327, 3, 23);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446328, 4, 8);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446329, 5, 12);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446330, 6, 17);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446331, 7, 2);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446332, 8, 11);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446333, 9, 7);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446334, 10, 13);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446335, 11, 16);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446336, 12, 3);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446337, 13, 9);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446338, 14, 21);
INSERT INTO public.likes (upd, userid, likecount) VALUES (1630446339, 15, 4);
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
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446325, 1, 'A beautiful sunset', '2022-04-24', 'image1.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446326, 2, 'A delicious meal', '2022-04-24', 'image2.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446327, 3, 'A view from the top', '2022-04-24', 'image3.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446328, 4, 'Pushing past limits', '2022-04-24', 'image4.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446329, 5, 'Concert vibes', '2022-04-24', 'image5.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446330, 6, 'Movie night', '2022-04-24', 'image6.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446331, 7, 'Getting lost in a good book', '2022-04-24', 'image7.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446332, 8, 'Stylish outfit', '2022-04-24', 'image8.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446333, 9, 'Artistic expression', '2022-04-24', 'image9.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446334, 10, 'Capturing a moment in time', '2022-04-24', 'image10.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446335, 11, 'Enjoying the great outdoors', '2022-04-24', 'image11.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446336, 12, 'Playing sports', '2022-04-24', 'image12.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446337, 13, 'Managing finances', '2022-04-24', 'image13.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446338, 14, 'Staying healthy', '2022-04-24', 'image14.png');
INSERT INTO public.photos (upd, uad, caption, data, filepath) VALUES (1630446339, 15, 'Political activism', '2022-04-24', 'image15.png');


ALTER TABLE public.photos OWNER TO "rootUser";

--
-- Name: tags; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.tags (
    tag character varying NOT NULL,
    upd integer
);

INSERT INTO public.tags (tag, upd) VALUES ('technology', 1630446325);
INSERT INTO public.tags (tag, upd) VALUES ('food', 1630446326);
INSERT INTO public.tags (tag, upd) VALUES ('travel', 1630446327);
INSERT INTO public.tags (tag, upd) VALUES ('fitness', 1630446328);
INSERT INTO public.tags (tag, upd) VALUES ('music', 1630446329);
INSERT INTO public.tags (tag, upd) VALUES ('movies', 1630446330);
INSERT INTO public.tags (tag, upd) VALUES ('books', 1630446331);
INSERT INTO public.tags (tag, upd) VALUES ('fashion', 1630446332);
INSERT INTO public.tags (tag, upd) VALUES ('art', 1630446333);
INSERT INTO public.tags (tag, upd) VALUES ('photography', 1630446334);
INSERT INTO public.tags (tag, upd) VALUES ('nature', 1630446335);
INSERT INTO public.tags (tag, upd) VALUES ('sports', 1630446336);
INSERT INTO public.tags (tag, upd) VALUES ('finance', 1630446337);
INSERT INTO public.tags (tag, upd) VALUES ('health', 1630446338);
INSERT INTO public.tags (tag, upd) VALUES ('politics', 1630446339);

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
);

INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (301, 'Aiden', 'Smith', 'aiden.smith@asu.edu', '1999-03-14', 'Phoenix', 'M', 'password1', 2);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (302, 'Brianna', 'Johnson', 'brianna.johnson@asu.edu', '2000-06-22', 'Tucson', 'F', 'password2', 3);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (303, 'Caleb', 'Williams', 'caleb.williams@asu.edu', '1998-12-30', 'Mesa', 'M', 'password3', 5);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (304, 'Danielle', 'Brown', 'danielle.brown@asu.edu', '1999-11-18', 'Glendale', 'F', 'password4', 1);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (305, 'Ethan', 'Jones', 'ethan.jones@asu.edu', '1998-08-05', 'Scottsdale', 'M', 'password5', 4);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (306, 'Fiona', 'Garcia', 'fiona.garcia@asu.edu', '2000-04-27', 'Chandler', 'F', 'password6', 3);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (307, 'Gavin', 'Miller', 'gavin.miller@asu.edu', '1999-02-12', 'Gilbert', 'M', 'password7', 2);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (308, 'Hailey', 'Wilson', 'hailey.wilson@asu.edu', '1998-07-08', 'Tempe', 'F', 'password8', 1);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (309, 'Isaac', 'Moore', 'isaac.moore@asu.edu', '2000-05-19', 'Peoria', 'M', 'password9', 4);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (310, 'Jasmine', 'Taylor', 'jasmine.taylor@asu.edu', '1999-10-25', 'Yuma', 'F', 'password10', 3);
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (311, 'Jay', 'Bloc', 'jbloc@asu.edu', '1998-09-30', 'Flagstaff', 'M', 'password11', 2)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (312, 'Kodak', 'Black', 'kblack@asu.edu', '1999-10-30', 'Oro Heights', 'M', 'password12', 2)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (313, 'Young', 'Thug', 'ythug@asu.edu', '1997-03-20', 'LA', 'M', 'password13', 2)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (314, 'Quavo', 'Migos', 'quavo@asu.edu', '1999-04-10', 'San Dimas', 'M', 'password14', 2)
INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) VALUES (315, 'SHOW', 'GALANTIS', 'galantis@asu.edu', '1991-01-10', 'The Valley', 'M', 'password15', 2)
ALTER TABLE public.users OWNER TO "rootUser";

--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: rootUser
--

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

