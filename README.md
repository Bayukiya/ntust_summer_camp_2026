markdown
# NTUST Advanced Robotics & MLOps Academy (2026)

This repository contains the core software infrastructure, environment configurations, and baseline lesson modules for the **2026 NTUST Advanced Robotics and Systems Track**. 

The curriculum focuses on bridging the gap between raw data analysis/deep learning models and real-time execution layers using **ROS 2 (Robot Operating System)**, **ros2_control frameworks**, and **Gazebo physics engines**.

---

## 🛰️ System Architecture & Framework Matrix

To prevent the common architectural failure modes where unstructured code causes real-time lag or loop breakdowns, the workspace leverages a deterministic multi-tier software hierarchy:

Use code with caution.
┌──────────────────────────────────────────┐
│          High-Level AI Logic             │
│   (Computer Vision, VLM, Telemetry)      │
└────────────────────┬─────────────────────┘
│  (ROS 2 Topics/Actions)
┌────────────────────▼─────────────────────┐
│           Middle System: ROS 2           │
│      (move_group, Lifecycle Nodes)       │
└────────────────────┬─────────────────────┘
│  (Hardware Interfaces)
┌────────────────────▼─────────────────────┐
│         Real-Time Execution Layer        │
│     (ros2_control, Gazebo / HW)          │
└──────────────────────────────────────────┘

---

## ⚙️ Core Curriculum Tracking & Workspace Content

### 📁 `infrastructure/` (System Baselines)
Contains the verified build sheets (`all_installed_apt_packages.txt` and `manual_installed_packages.txt`) representing the exact system image baseline required for deterministic compilation across clusters.
* **Determinism Verification:** Enforces uniform CUDA toolkit layers and underlying client libraries (`_apt` handles, `rclcpp`, or `rclpy`) across individual workstations.

### 📦 `src/` Modules (Chronological Execution Engines)

#### Module 1: ROS 2 Node Architecture & Advanced Multi-Threading
* **Focus:** Implementation of `SingleThreadedExecutor`, `MultiThreadedExecutor`, and dedicated `Callback Groups` (CG) to completely eliminate race conditions and callback deadlocks during multi-sensor polling loops.
* **Topics:** Mutually Exclusive vs. Reentrant Callback Groups, custom executors, and system parameters configuration files (`.yaml`).

#### Module 2: Unified Robot Description & Kinematics (`urdf/` & `xacro/`)
* **Focus:** Constructing robust structural topologies for manipulators using Denavit-Hartenberg (DH) parameters, parametrized XML macros (`xacro`), and Semantic Robot Descriptions (`SRDF`).
* **Topics:** Link mass profiling, transform broad/listeners trees via `tf2`, and coordinate frame alignment conventions (REP-103/REP-105).

#### Module 3: Real-Time Closed-Loop System Control (`ros2_control`)
* **Focus:** Writing high-speed, real-time safe hardware abstraction layers (HAL).
* **Topics:** `controller_manager` configuration, lifecycle-managed state routing (`on_configure`, `on_activate`), state/command interface boundaries, and cascade control loops.

#### Module 4: High-Fidelity Physics Simulation (Gazebo Sim)
* **Focus:** Designing simulation worlds using Simulation Description Format (SDF) and synchronizing computer clock walls to Simulation Time with clean real-time factors (RTF).
* **Topics:** Physics plugin construction, multi-contact mechanics parsing, and sensor noise simulation pipelines.

---

## 🐳 Reproducible Deployment Setup

To instantly spin up the unified cluster workspace and run sample bring-up routines, compile using your target virtual workspace or direct container environments:

```bash
# 1. Source your environmental core package registry
source /opt/ros/jazzy/setup.bash

# 2. Build local editable source packages 
colcon build --symlink-install

# 3. Initialize the complete system orchestration dashboard
ros2 launch ntust_bringup start_system.launch.py
```

---

## 📜 Citation

If you reference this curriculum mapping tool or the underlying modular packaging mechanics in your academic research or lab courses, cite using this format:

```bibtex
@software{Kune_NTUST_Camp_2026,
  author       = {Kune, Bayisa},
  title        = {{NTUST-Summer-Camp-2026: An Advanced ROS 2 and MLOps Training Repository}},
  year         = {2026},
  month        = {June},
  version      = {1.0.0},
  publisher    = {GitHub},
  url          = {https://github.com}
}
```
