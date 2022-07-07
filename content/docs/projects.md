+++
title = "Projects"
author = ["Hrishikesh Barman"]
draft = false
+++

Link to project idea list. Describe what is project list and what is project idea list.
This page is about how I manage my projects, the table list. [project ideas](/project_ideas.html)

```emacs-lisp
;; (defun test/get-property-at-heading ()
;;   (let ((el (org-element-at-point)))
;;     (append table '((1 2 3)))
;;     ;(org-set-property "foo" (org-element-property :title el))))

;; function (org-map-entries #'test/get-property-at-heading))

(defun test/set-property-at-heading ()
  (let ((el (org-element-at-point)))
    ;(append table '((1 2 3)))
    ;(org-set-property "foo" (org-element-property :title el))))
    (org-set-property "foo" "poopppp")))

(org-map-entries #'test/set-property-at-heading "TABLE_ENTRY<>\"skip\"+LEVEL=1")
```

<a id="table--projects"></a>

| a | b | c | d |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |

| a | b | c | d |
|---|---|---|---|
|   |   |   |   |


## Keeping track {#keeping-track}

-   [Open Startup - Nomad List](https://nomadlist.com/open)
-   [Simple Analytics financial and customer happiness metrics](https://simpleanalytics.com/open)
-   [Stats - Luke's Wild Website](https://www.lkhrs.com/stats/)
-   [Stats : Website · roytang.net](https://roytang.net/page/stats/site/)
-   [Open Startup Metrics - Bannerbear](https://www.bannerbear.com/open/)


## Inspiration {#inspiration}

-   [Tristan's Site - Tristan Hume](https://thume.ca/) : like how their presents his projects
-   [It's Nicky Case!](https://ncase.me/)
-   [Danielle Baskin](https://daniellebaskin.com/) : Love how this guy is presenting his work, what i want to do very closely relates to his work
-   [Projects - Josh Pigford](https://joshpigford.com/projects) : Again love how he's showing his work, similar vein of work.
