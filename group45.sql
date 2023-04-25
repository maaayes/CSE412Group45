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
(100, ‘Travel’, 2, ‘2023-03-01’),
(101, ‘Food’, 3, ‘2023-01-27’),
(102, ‘Friends’, 3, ‘2022-08-10’),
(103, ‘Family’, 4, ‘2022-12-22’),
(104, ‘Random’, 6, ‘2022-10-03’),
(105, ‘Events’, 6, ‘2023-02-19’),
(106, ‘Nature’, 8, ‘2023-05-28’),
(107, ‘Photos’, 9, ‘2021-12-12’),
(108, ‘Summer’, 9, ‘2022-12-29’),
(109, ‘Family’, 10, ‘2022-11-30’),
(110, ‘Vacations’, 11, ‘2023-04-22’),
(111, ‘College’, 11, ‘2023-04-22’),
(112, ‘Holidays’, 12, ‘2023-04-22’),
(113, ‘Camping’, 13, ‘2023-04-22’);

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
(20000, 'looks good', 1, 10002, '2023-01-28'),
(20001, 'that was fun', 1, 10003, '2022-08-11'),
(20002, 'have a great trip', 2, 10000, '2023-03-02'),
(20003, 'looks like fun', 3, 10000, '2023-03-02'),
(20004, 'great picture', 4, 10000, '2023-03-03'),
(20005, 'really nice', 5, 10008, '2023-05-29'),
(20006, 'it was great', 7, 10010, '2022-12-31'),
(20007, 'really nice', 7, 10004, '2022-12-23'),
(20008, 'looks great', 8, 10002, '2023-01-28'),
(20009, 'amazing', 9, 10005, '2022-10-04'),
(20010, 'great job', 10, 10006, '2023-02-20'),
(20011, 'congratulations', 10, 10007, '2023-02-20'),
(20012, 'good luck’, 10, 10013, '2023-02-01'),
(20013, 'have fun', 6, 10016, '2023-04-22’),
(20014, ‘happy holidays’', 14, 10014, '2023-04-22'),
(20015, 'happy valentines day', 14, 10015, '2023-04-22'),
(20016, 'this is cute', 11, 10015, '2023-04-22');

ALTER TABLE public.comments OWNER TO "rootUser";

--
-- Name: friends; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.friends (
    userid integer NOT NULL,
    friend integer,
    friendshipdate date
);


INSERT INTO public.friends (userid, friend, friendshipDate)
VALUES
(1, 6, '2023-03-01'),
(2, 9, '2023-01-27'),
(3, 4, '2022-08-10'),
(4, 3, '2022-12-22'),
(5, 10, '2022-10-03'),
(6, 1, '2023-02-19'),
(7, 6, '2023-05-28'),
(8, 10, '2021-12-12'),
(9, 7, '2022-12-29'),
(10, 5, '2023-01-30'),
(11, 2, '2023-04-22'),
(12, 14, '2023-04-22'),
(13, 6, '2023-04-22'),
(14, 12, '2023-04-22');

ALTER TABLE public.friends OWNER TO "rootUser";

--
-- Name: likes; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.likes (
    upd integer NOT NULL,
    userid integer,
    likecount integer
);

INSERT INTO public.likes (upd, userid, likecount)
VALUES 
(10000, 1, 0),
(10001, 1, 10),
(10002, 2, 2),
(10003, 2, 21),
(10004, 3, 4),
(10005, 5, 29),
(10006, 5, 7),
(10007, 5, 0),
(10008, 7, 10),
(10009, 8, 23),
(10010, 8, 47),
(10011, 9, 12),
(10012, 10, 9),
(10013, 10, 14),
(10014, 11, 2),
(10015, 11, 0),
(10016, 12, 3);

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

INSERT INTO public.photos (upd, uad, caption, data, filepath)
VALUES
(10000, 100, ‘my fav trip’, , ),
(10001, 100, ‘europe 2022’, , ),
(10002, 101, ‘fav restaurant’, , ),
(10003, 102, ‘my friends’, , ),
(10004, 103, ‘my family’, , ),
(10005, 104, ‘extra photos’, , ),
(10006, 105, ‘graduation event’, , ),
(10007, 105, ‘wedding event’, , ),
(10008, 106, ‘the beach’, , ),
(10009, 107, ‘my fav photo’, , ),
(10010, 108, ‘last summer was fun’, , ),
(10011, 109, ‘thanksgiving with family’, , ),
(10012, 110, ‘exploring the city’, , ),
(10013, 111, ‘first day of the semester’, , ),
(10014, 112, ‘christmas 2022’, , ),
(10015, 112, ‘vday 2023’, , ),
(10016, 113, ‘setting up camp’, , );

ALTER TABLE public.photos OWNER TO "rootUser";


--
-- Name: tags; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.tags (
    tag character varying,
    upd integer NOT NULL
);

INSERT INTO public.tags (tag, upd)
VALUES 
('trip', 10000),
('fun', 10000),
('favorite', 10002),
('friends', 10003),
('family', 10004),
('yay', 10006),
('congrats', 10006),
('happy', 10007),
('ocean', 10008),
('favorite', 10009),
('boston', 10010),
('boston', 10011),
('nyc', 10012),
(‘merry’, 10014),
(‘love’, 10015),
('outdoors', 10016);

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

INSERT INTO public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum)
VALUES
(1, 'John', 'Smith', 'jsmith@gmail.com', '2000-05-03', 'Phoenix', 'M', 'smith12', 0),
(2, 'Mary', 'James', 'mjames@gmail.com', '1998-11-21', 'Seattle', 'F', 'james34', 1),
(3, 'Noah', 'Miller', 'nmiller@gmail.com', '2001-02-14', 'Phoenix', 'M', 'miller56', 2),
(4, 'Olivia', 'Johnson', 'ojohnson@gmail.com', '1999-09-08', 'Springfield', 'F', 'john78', 1),
(5, 'Sam', 'Williams', 'swilliams@gmail.com', '2003-06-25', 'Franklin', 'M', 'will90', 0),
(6, 'Nicole', 'Wilson', 'nwilson@gmail.com', '2000-12-17', 'Madison', 'F', 'wilson22', 2),
(7, 'Sara', 'Miller', 'smiller@gmail.com', '2001-10-30', 'Oakland', 'F', 'mill35', 0),
(8, 'Mike', 'Jones', 'mjones@gmail.com', '1993-04-23', 'Denver', 'M', 'jones09', 1),
(9, 'Lisa', 'Davis', 'ldavis@gmail.com', '2002-07-16', 'Boston', 'F', 'davis23', 2),
(10, 'Liam', 'Brown', 'lbrown@gmail.com', '1997-03-24', 'Chicago', 'M', 'brown79', 1),
(11, ‘Alex’, ‘Kim’, ‘akim@gmail.com', '1999-05-05', ‘Miami’, 'M', 'kim80', 2),
(12, ‘Jasmine’, 'Chen', ‘jchen@gmail.com', '1998-01-14', 'Seattle', 'F', 'chen00', 1),
(13, ‘Ava’, 'Martin', 'amartin@gmail.com', '1994-12-03', ‘Detroit’, 'F', 'martin97', 1),
(14, 'Ethan', 'Anderson', 'eanderson@gmail.com', '1997-09-24', 'Phoenix', 'M', 'anderson14', 0);

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
1	aba	aba	2@gmail.co	2023-04-23	cshu	Male	2	0
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
-- Name: comments comments_upd_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_upd_key UNIQUE (upd);


--
-- Name: comments comments_userid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_userid_key UNIQUE (userid);


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
-- Name: photos photos_uad_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_uad_key UNIQUE (uad);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (upd);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- PostgreSQL database dump complete
--

